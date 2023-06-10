const express = require("express");
const app = express();
const mongoose = require("mongoose");
const dotenv = require("dotenv");
dotenv.config();
const cors = require("cors");
const port = process.env.PORT || 8080;

app.use(cors());

app.use(express.json());
const authRoute = require("./Routes/auth");

mongoose
    .connect(process.env.MONGO_URL, {
        useNewUrlParser: true,
    })
    .then(console.log(`Connected to MONGO_DB`))
    .catch((err) => {
        console.log(err);
    });

app.use("/auth", authRoute);

app.listen(port, (err) => {
    if (err) console.log(err);
    else console.log(`Server started at port:${port}`);
});
