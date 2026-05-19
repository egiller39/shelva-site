const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const outDir = path.join(root, 'dist');
const maxAssetBytes = 25 * 1024 * 1024;

const rootFiles = [
  '_headers',
  'app-redirect.html',
  'contact.html',
  'design.html',
  'favicon.ico',
  'favicon.png',
  'features.html',
  'how-it-works.html',
  'icon.png',
  'icon2.png',
  'index.html',
  'mobile-menu.js',
  'partners.html',
  'policy.html',
  'pricing.html',
  'release-notes.html',
  'robots.txt',
  'shelva-48.png',
  'shelva-logo-square.png',
  'sitemap.xml',
  'starter-kit.html',
  'technology.html',
  'template.html',
];

const skipFiles = new Set([
  path.normalize('images/live-media/black-rose/Poke-horizontal-pan.gif'),
  path.normalize('images/live-media/black-rose/Poke-innout.gif'),
]);

function copyFile(source, destination) {
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.copyFileSync(source, destination);
}

function copyDirectory(sourceDir, destinationDir, relativeBase = '') {
  for (const entry of fs.readdirSync(sourceDir, { withFileTypes: true })) {
    const sourcePath = path.join(sourceDir, entry.name);
    const relativePath = path.join(relativeBase, entry.name);
    const destinationPath = path.join(destinationDir, entry.name);

    if (entry.isDirectory()) {
      copyDirectory(sourcePath, destinationPath, relativePath);
      continue;
    }

    if (!entry.isFile()) {
      continue;
    }

    const normalizedRelativePath = path.normalize(path.join('images', relativePath));
    const size = fs.statSync(sourcePath).size;

    if (skipFiles.has(normalizedRelativePath) || size > maxAssetBytes) {
      console.log(`Skipping oversized Pages asset: ${normalizedRelativePath}`);
      continue;
    }

    copyFile(sourcePath, destinationPath);
  }
}

fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(outDir, { recursive: true });

for (const file of rootFiles) {
  const source = path.join(root, file);
  if (fs.existsSync(source)) {
    copyFile(source, path.join(outDir, file));
  }
}

copyDirectory(path.join(root, 'images'), path.join(outDir, 'images'));
