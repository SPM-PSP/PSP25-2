// Create OS desktop notifications
//
// For more info, see:
// https://electronjs.org/docs/api/notification
// https://electronjs.org/docs/tutorial/notifications

const { app, BrowserWindow, Notification } = require('electron/main')
const path = require('node:path')
const parser = require('./src/parser')

app.whenReady().then(() => {
  const mainWindow = new BrowserWindow({
    height: 600,
    width: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  data = parser.parseJson()

  if (Notification.isSupported()) {
    const notification = new Notification({
      title: 'Notification!',
      subtitle: 'Data from model',
      body: `${Object.keys(data)[0]}: ${data[Object.keys(data)[0]]}\n${Object.keys(data)[1]}: ${data[Object.keys(data)[1]]}`,
      hasReply: true
    })

    notification.on('show', () => console.log('Notification shown'))
    notification.on('click', () => console.log('Notification clicked'))
    notification.on('close', () => console.log('Notification closed'))
    notification.on('reply', (event, reply) => {
      console.log(`Reply: ${reply}`)
    })

    notification.show()
  } else {
    console.log('Hm, are notifications supported on this system?')
  }

  mainWindow.loadFile('index.html')
})
