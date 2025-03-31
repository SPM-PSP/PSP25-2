const fs = require('fs');
const path = require('path');

// Function to parse the JSON file
function parseJson() {
    const filePath = path.join(__dirname, '../data/example.json');
    
    try {
        // Read the file
        const fileContent = fs.readFileSync(filePath, 'utf-8');
        
        // Parse the JSON content
        const data = JSON.parse(fileContent);
        
        // Process the data (customize this based on your JSON structure)
        console.log('Parsed Data:', data);
        return data;
    } catch (error) {
        console.error('Error parsing JSON file:', error.message);
        return null;
    }
}

module.exports = {
    parseJson
}
