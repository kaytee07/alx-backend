import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', async () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`)
})

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
    try {
	const response = await getAsync(schoolName);
	console.log(response)
    } catch(error) {
	console.error(error);
    }
};

const call = async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

call();
