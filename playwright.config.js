import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['html', { 
      outputFolder: 'playwright-report', // Corrected property name
      open: 'never'  // Disable the report server from starting
    }]
  ],
  // Optional: Set the timeout for test execution or other configurations as needed
});
