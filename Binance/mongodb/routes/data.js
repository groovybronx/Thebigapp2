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
    try {
        const db = mongoose.connection.client.db(dbName);
        const collections = await db.listCollections().toArray();
        const collectionData = {};

        for (const collection of collections) {
            const collectionName = collection.name;
            const documents = await db.collection(collectionName).find().toArray();
            collectionData[collectionName] = documents;
        }

        res.render('database', { dbName, collections, collectionData });
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la récupération des données de la base de données');
    }
});

// Routes des collections (dans la page database)
router.post('/database/:dbName/:collectionName', async (req, res) => {
    const dbName = req.params.dbName;
    const collectionName = req.params.collectionName;
    try {
        const db = mongoose.connection.client.db(dbName);
        const collection = db.collection(collectionName);
        await collection.insertOne(req.body);
        res.redirect(`/data/database/${dbName}`);
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de l\'ajout du document');
    }
});

router.get('/database/:dbName/:collectionName/delete/:id', async (req, res) => {
    const dbName = req.params.dbName;
    const collectionName = req.params.collectionName;
    const id = req.params.id;
    try {
        const db = mongoose.connection.client.db(dbName);
        const collection = db.collection(collectionName);
        await collection.deleteOne({ _id: mongoose.Types.ObjectId(id) });
        res.redirect(`/data/database/${dbName}`);
    } catch (err) {
        console.error(err);
        res.status(500).send('Erreur lors de la suppression du document');
    }
});

module.exports = router;