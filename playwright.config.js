import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    screenshot: 'only-on-failure', // Take screenshots only on test failure
    video: 'off', // Disable video recording
  },
  reporter: [
    ['html', { 
      outputFolder: 'playwright-report', // Save the report to a folder
      open: 'never'  // Disable the report server from starting
    }]
  ],
});
