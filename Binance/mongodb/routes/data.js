const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');

// Routes des bases de données
router.get('/', async (req, res) => {
    try {
        const db = mongoose.connection.db;
        const adminDb = db.admin();
        const databases = await adminDb.listDatabases();
        const databasesArray = databases.databases || [];
        res.render('index', { databases: databasesArray });
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la récupération des bases de données');
    }
});

router.post('/createDatabase', async (req, res) => {
    const dbName = req.body.dbName;
    try {
        const newDb = mongoose.connection.client.db(dbName);
        const tempCollection = newDb.collection('tempCollection');
        await tempCollection.insertOne({ temp: true });
        res.redirect('/data');
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la création de la base de données');
    }
});

router.get('/deleteDatabase/:dbName', async (req, res) => {
    const dbName = req.params.dbName;
    try {
        await mongoose.connection.client.db(dbName).dropDatabase();
        res.redirect('/data');
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la suppression de la base de données');
    }
});

router.get('/database/:dbName', async (req, res) => {
    const dbName = req.params.dbName;
    const filter = req.query.filter ? JSON.parse(req.query.filter) : {};
    const sort = req.query.sort ? JSON.parse(req.query.sort) : {};
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const skip = (page - 1) * limit;
    const selectedCollection = req.query.collection;

    try {
        const db = mongoose.connection.client.db(dbName);
        const collections = await db.listCollections().toArray();
        const userCollections = collections.filter(collection => !collection.name.startsWith('system.'));

        const collectionData = selectedCollection ? {
            [selectedCollection]: await db.collection(selectedCollection).find(filter).sort(sort).skip(skip).limit(limit).toArray()
        } : {};

        const collectionCounts = selectedCollection ? {
            [selectedCollection]: await db.collection(selectedCollection).countDocuments(filter)
        } : {};

        res.render('database', { dbName, collections: userCollections, collectionData, filter: JSON.stringify(filter), sort: JSON.stringify(sort), page, limit, selectedCollection, collectionCounts });
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la récupération des données de la base de données');
    }
});

// Route pour créer une nouvelle collection
router.post('/database/:dbName/createCollection', async (req, res) => {
    const dbName = req.params.dbName;
    const collectionName = req.body.collectionName;
    try {
        const db = mongoose.connection.client.db(dbName);
        await db.createCollection(collectionName);
        res.redirect(`/data/database/${dbName}`); // Rediriger vers la page de la base de données
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la création de la collection');
    }
});

// Route pour renommer une collection
router.get('/database/:dbName/renameCollection/:collectionName', async (req, res) => {
    const dbName = req.params.dbName;
    const collectionName = req.params.collectionName;
    try {
        // Logique pour renommer la collection
        const newName = req.query.newName; // Récupérer le nouveau nom de la collection depuis la requête
        const db = mongoose.connection.client.db(dbName);
        await db.collection(collectionName).rename(newName);
        res.redirect(`/data/database/${dbName}`); // Rediriger vers la page de la base de données
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors du renommage de la collection');
    }
});

// Route pour effacer une collection
router.get('/database/:dbName/deleteCollection/:collectionName', async (req, res) => {
    const dbName = req.params.dbName;
    const collectionName = req.params.collectionName;
    try {
        const db = mongoose.connection.client.db(dbName);
        await db.collection(collectionName).drop();
        res.redirect(`/data/database/${dbName}`); // Rediriger vers la page de la base de données
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la suppression de la collection');
    }
});

module.exports = router;