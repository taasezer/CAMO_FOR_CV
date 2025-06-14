const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/search', (req, res) => {
    const name = req.body.name;
    const dataDir = path.join(__dirname, 'DATASERVICE');
    const files = fs.readdirSync(dataDir).filter(file => file.includes(name));

    res.json({ files });
});

app.listen(port, () => {
    console.log(`Sunucu ${port} portunda çalışıyor.`);
});
