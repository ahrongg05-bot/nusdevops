
import { test, expect, Page } from '@playwright/test';

const baseURL = 'https://www.saucedemo.com/';
// doesnt work async function login(page) 
async function login(page: Page) {

  await page.goto(baseURL);

  await page.getByPlaceholder('Username').fill('standard_user');
  await page.getByPlaceholder('Password').fill('secret_sauce');
  await page.getByRole('button', { name: 'Login' }).click();

  await expect(page.getByText('Products')).toBeVisible();
}


// Task 1 - Successful login
test('successful login with valid credentials', async ({ page }) => {
  await login(page);

  await expect(page).toHaveURL(/inventory/);
  await expect(page.getByText('Products')).toBeVisible();
});


// Task 1 - Invalid login
test('shows error message for invalid credentials', async ({ page }) => {
  await page.goto(baseURL);

  await page.getByPlaceholder('Username').fill('invalid_user');
  await page.getByPlaceholder('Password').fill('wrong_password');

  await page.getByRole('button', { name: 'Login' }).click();

  await expect(
    page.getByText(/Username and password do not match/)
  ).toBeVisible();
});


// Task 2 + Task 3
test('add products to cart and complete checkout', async ({ page }) => {

  // Login
  await login(page);

  // Add two products
await page.locator('#add-to-cart-sauce-labs-backpack').click();
await page.locator('#add-to-cart-sauce-labs-bike-light').click();

  // Verify cart badge shows 2
await expect(page.locator('.shopping_cart_badge')).toHaveText('2');

  // Open cart
await page.locator('.shopping_cart_link').click();

  // Verify products are in cart
await expect(page.getByText('Sauce Labs Backpack')).toBeVisible();
await expect(page.getByText('Sauce Labs Bike Light')).toBeVisible();

  // Proceed to checkout
  await page.getByRole('button', { name: 'Checkout' }).click();

  // Fill customer information
  await page.getByPlaceholder('First Name').fill('John');
  await page.getByPlaceholder('Last Name').fill('Tan');
  await page.getByPlaceholder('Zip/Postal Code').fill('123456');

  await page.getByRole('button', { name: 'Continue' }).click();

  // Complete order
  await page.getByRole('button', { name: 'Finish' }).click();

  // Verify confirmation
  await expect(
    page.getByText('Thank you for your order!')
  ).toBeVisible();
});