import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['html', { 
      outputFile: 'playwright-report/index.html', // Save the report to a file
      open: 'never'  // Disable the report server from starting
    }]
  ],
  // Optional: Set the timeout for test execution or other configurations as needed
});
