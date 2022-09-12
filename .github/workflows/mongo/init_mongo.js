db.createUser(
        {
            user: "weaverusr",
            pwd: "weaverpass",
            roles: [
                {
                    role: "readWrite",
                    db: "weaverdb"
                }
            ]
        }
);
