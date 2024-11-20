import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['html', { outputFile: 'playwright-report/index.html' }]
  ], // Generates report without serving it
});
