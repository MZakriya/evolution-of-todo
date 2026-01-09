import { betterAuth } from "better-auth";
import { neonServerlessDriver } from "@neondatabase/serverless";

// 1. Force verify that DATABASE_URL exists
if (!process.env.DATABASE_URL) {
    throw new Error("❌ DATABASE_URL is missing in environment variables");
}

// 2. Configure Better Auth with Neon serverless driver for proper SSL handling
export const auth = betterAuth({
    database: {
        provider: "postgresql",
        url: process.env.DATABASE_URL,
        driver: neonServerlessDriver({
            connectionString: process.env.DATABASE_URL,
        }),
    },
    emailAndPassword: {
        enabled: true,
    },
    // Add trusted origins for CORS
    trustedOrigins: ["http://localhost:3000"],
});