require('dotenv').config({ path: './.env.local' });
const { Pool } = require('pg');

// Create a manual Postgres Pool with Explicit SSL
const pool = new Pool({
    connectionString: process.env.DATABASE_URL,
    ssl: {
        rejectUnauthorized: false // CRITICAL for Neon in Dev/Node environments
    },
    max: 10, // Connection limit
    idleTimeoutMillis: 30000
});

async function testConnection() {
    console.log('Testing database connection...');

    if (!process.env.DATABASE_URL) {
        console.log('❌ DATABASE_URL is missing in environment variables');
        return;
    }

    const client = await pool.connect();

    try {
        // Run a simple query
        const result = await client.query('SELECT NOW()');
        console.log('✅ Database Connection Successful');
        console.log('Current time from database:', result.rows[0].now);
    } catch (error) {
        console.log('❌ Database Connection Failed');
        console.log('Error details:', error.message);
    } finally {
        client.release();
        await pool.end();
    }
}

testConnection()
    .then(() => {
        console.log('Diagnostic completed');
        process.exit(0);
    })
    .catch((error) => {
        console.error('Diagnostic failed:', error);
        process.exit(1);
    });