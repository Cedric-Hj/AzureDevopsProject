import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['json', { outputFile: 'playwright-report/results.json' }],  // Save results in JSON format
    ['html', { outputFile: 'playwright-report/index.html', open: 'never' }]  // Save HTML but prevent server
  ],
  // Optional: Set the timeout for test execution or other configurations as needed
});
