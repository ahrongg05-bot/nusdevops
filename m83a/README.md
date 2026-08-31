ACTION STEPS

mkdir m83a
cd m83a
npm init playwright@latest


Do you want to use TypeScript or JavaScript?
> TypeScript

Where to put your end-to-end tests?
> tests

Add a GitHub Actions workflow?
> false

Install Playwright browsers?
> true


after install
m83a
│
├── node_modules
├── tests
│   └── example.spec.ts
│
├── package.json
├── package-lock.json
└── playwright.config.ts


rm tests/example.spec.ts. (remove)
touch tests/shopping-flow.spec.ts (create )
add the code base in tests/shopping-flow.spec.ts 
then run npx playwright test

[screenshot of playwright test](image.png)

then run npx playwright test --headed
[This Playwright UI showing successful checkout](image-1.png)



https://cs4218.github.io/user-guide/contents/topic1b.html

