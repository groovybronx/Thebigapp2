const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const dataRoutes = require('./routes/data'); // Chemin modifié
const config = require('./config'); // Importez le fichier de configuration

const app = express();
const port = 3000;

// Connexion à MongoDB Atlas
mongoose
  .connect(config.mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connexion à MongoDB Atlas réussie'))
  .catch((err) => console.error(err));

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/data', dataRoutes);

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});