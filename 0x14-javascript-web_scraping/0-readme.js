const fs = require('fs');

const fileName = process.argv[2];

if (process.argv.length < 3) {
  console.log('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}
);
