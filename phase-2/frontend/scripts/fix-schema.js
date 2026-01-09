require('dotenv').config({ path: './.env.local' });
const { Client } = require('pg');

async function fixUserSchema() {
    const client = new Client({
        connectionString: process.env.DATABASE_URL,
        ssl: {
            rejectUnauthorized: false // CRITICAL for Neon in Dev/Node environments
        }
    });

    try {
        await client.connect();
        console.log('Connected to database');

        // Execute the SQL commands to add missing columns to the user table
        await client.query(`
            ALTER TABLE "user" ADD COLUMN IF NOT EXISTS "name" TEXT;
        `);
        console.log('Added name column if not exists');

        await client.query(`
            ALTER TABLE "user" ADD COLUMN IF NOT EXISTS "emailVerified" BOOLEAN DEFAULT FALSE;
        `);
        console.log('Added emailVerified column if not exists');

        await client.query(`
            ALTER TABLE "user" ADD COLUMN IF NOT EXISTS "image" TEXT;
        `);
        console.log('Added image column if not exists');

        await client.query(`
            ALTER TABLE "user" ADD COLUMN IF NOT EXISTS "createdAt" TIMESTAMP DEFAULT NOW();
        `);
        console.log('Added createdAt column if not exists');

        await client.query(`
            ALTER TABLE "user" ADD COLUMN IF NOT EXISTS "updatedAt" TIMESTAMP DEFAULT NOW();
        `);
        console.log('Added updatedAt column if not exists');

        console.log('✅ User Schema Repaired');

    } catch (error) {
        console.error('Error repairing user schema:', error);
        throw error;
    } finally {
        await client.end();
    }
}

fixUserSchema()
    .then(() => {
        console.log('Schema repair completed successfully');
        process.exit(0);
    })
    .catch((error) => {
        console.error('Schema repair failed:', error);
        process.exit(1);
    });