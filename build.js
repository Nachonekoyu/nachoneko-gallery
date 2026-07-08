const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const distDir = './dist';

if (fs.existsSync(distDir)) {
    execSync(`rm -rf ${distDir}`);
}

fs.mkdirSync(distDir, { recursive: true });

function copyDir(src, dest) {
    if (!fs.existsSync(dest)) {
        fs.mkdirSync(dest, { recursive: true });
    }
    
    const entries = fs.readdirSync(src, { withFileTypes: true });
    
    for (const entry of entries) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);
        
        if (entry.isDirectory()) {
            copyDir(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
        }
    }
}

const filesToCopy = [
    'index.html',
    'main-gallery.html',
    'emote-gallery.html',
    'characters.html',
    'images',
    '_headers',
    '_redirects'
];

filesToCopy.forEach(item => {
    if (fs.existsSync(item)) {
        const dest = path.join(distDir, item);
        if (fs.statSync(item).isDirectory()) {
            copyDir(item, dest);
        } else {
            fs.copyFileSync(item, dest);
        }
        console.log(`Copied: ${item}`);
    }
});

console.log('Build completed successfully!');