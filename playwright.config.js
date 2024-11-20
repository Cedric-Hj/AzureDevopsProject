import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on', // Enable video recording for all tests
  },
  reporter: [
    ['html', { 
      outputFolder: 'playwright-report', // Save the report to a folder
      open: 'never'  // Disable the report server from starting
    }]
  ],
});
