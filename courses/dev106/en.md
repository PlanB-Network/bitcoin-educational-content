---
name: Building a Lightning Wallet Backend
goal: Learn Bitcoin programming fundamentals and development to build practical Lightning Network applications and tools.
objectives:
  - Explore User authentication and authorization
  - Understand Lightning Network payments and invoices
  - Learn database operations for user and transaction data
  - Get into production deployment
---

# Course Overview

Unlock the power of server-side JavaScript and build scalable, high-performance applications. This course is designed for aspiring developers who want to master the Node.js ecosystem from the ground up. You will go from installing your first environment to deploying professional-grade APIs, learning about the event loop, asynchronous programming, and the massive NPM library along the way. Practical, project-based, and aligned with industry standards.

+++

# Introduction
<partId>b2642fea-3242-4ead-bda5-c02a8811d0fd</partId>

## Course overview
<chapterId>45922af8-b89c-47a9-b548-1900838dc55d</chapterId>

Welcome to the world of Node.js. In this initial chapter, we will explore why Node.js has become the industry standard for building fast and scalable network applications. We will break down the myth that "JavaScript is only for browsers" and see how the V8 engine allows us to run powerful code directly on servers.

### Prerequisites
* Basic knowledge of JavaScript (variables, functions, and objects).
* A code editor installed (VS Code recommended).
* Access to a terminal or command prompt.

### What we will build
We will start by creating a "System Information Tool," a small script that interacts with your operating system to display hardware stats, serving as your first step into the Node.js runtime.

Ready to dive into the fascinating world of Bitcoin Development, specifically the backend side,  and understand all its inner workings? Let's go!

# Node.js & Module System
<partId>d6635b9f-bef8-4c25-914a-c7431adb14a6</partId>

## Node.js Environment
<chapterId>986f478c-6780-4a64-a191-5816c8da454d</chapterId>

![Video](https://peertube.planb.network/videos/embed/69898b56-edd6-4e15-a38b-c904d3fcecf3)

### Introducing Node.js

Node.js is a **JavaScript runtime** built on the V8 engine that allows you to run JavaScript code outside of a web browser.

#### Key Components

##### The V8 Engine
- Open-source JavaScript engine developed by Google
- Designed to compile and execute JavaScript code at lightning-fast speeds
- The same engine that powers Google Chrome

##### Why Node.js Matters
Before Node.js, JavaScript was confined to the browser. Node.js breaks JavaScript out of its cage, enabling:
- **Server-side applications** - Build web servers and APIs
- **Command-line tools** - Create utilities and scripts
- **Desktop applications** - Build cross-platform apps
- **System-level access** - Interact with file systems, networks, and hardware

#### System-Level Resources
Running JavaScript outside the browser means developers can access:
- **File system** - Read and write files
- **Network sockets** - Handle real-time communication
- **Memory management** - Direct system resource access
- **Operating system APIs** - Interface with the underlying OS

### Server Environment vs Web Environment

#### Understanding the Difference

| Server Environment | Web Environment |
|-------------------|-----------------|
| Executes server-side code | Executes client-side code |
| Runs on secure, controlled servers | Runs in user's browser |
| Has full system access | Sandboxed for security |
| Serves data to clients | Consumes data from servers |
| Can be cloud-hosted or self-hosted | Depends on browser capabilities |

#### Client-Server Model
The **client-server model** is a fundamental concept in web development:
- **Server**: Holds and serves data, handles business logic, maintains security
- **Client**: Requests and displays data, handles user interactions
- **Communication**: Clients request resources from servers via APIs

#### Why Backend Development?
- **Data Security**: Sensitive operations happen on secure servers
- **Scalability**: Handle thousands of concurrent users
- **Business Logic**: Implement complex algorithms and data processing
- **API Creation**: Build interfaces for multiple client applications

### Node.js Capabilities

#### Popular Use Cases
- **Data streaming** - Real-time data processing
- **Server-side proxy** - Route and manage requests
- **Big data and analytics** - Process large datasets
- **Wireless connectivity** - IoT device communication
- **System monitoring** - Track resource usage
- **Real-time applications** - Chat apps, gaming, live updates
- **Web scraping** - Automated data collection
- **REST APIs** - The foundation of modern web services

## Modules and Packages
<chapterId>bf5ac02b-933a-479d-93dd-fbf47a427cf1</chapterId>

### Modules and the CommonJS System

##### What Are Modules?
Modules are self-contained units of code that:
- Keep code organized and manageable
- Have their own variables and functions
- Can be imported and exported between files
- Enable code reuse and sharing

##### CommonJS Module System
Node.js uses the CommonJS module system for importing and exporting code:

```javascript
// greeting.js - Creating a module
const greeting = "Hello, World!";
module.exports = greeting;

// index.js - Using a module
const greeting = require('./greeting');
console.log(greeting); // "Hello, World!"
```

##### Exporting Multiple Items
```javascript
// math.js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

module.exports = {
  add,
  subtract
};

// app.js
const { add, subtract } = require('./math');
console.log(add(5, 3)); // 8
```

### Node Package Manager (NPM)

##### What is NPM?
NPM is a package manager that:
- Provides access to over 1 million open-source packages
- Manages project dependencies
- Includes a command-line interface for easy package management
- Enables sharing your own packages with the community

##### Basic NPM Commands
```bash
npm --version          # Check NPM version
npm init -y           # Initialize a new project
npm install axios     # Install a package
npm install           # Install all dependencies
```

### Working with Built-in Modules
Node.js provides many built-in modules for common tasks:

```javascript
// File system operations
const fs = require('fs');
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Operating system information
const os = require('os');
console.log(os.platform());
console.log(os.architecture());
```


### Hands-on Mini Project: Command-Line Greeting App

Let's build a command-line application that greets users and displays the current date and time.

#### Project Setup
```bash
mkdir hello-node
cd hello-node
npm init -y
```

#### Complete Code
```javascript
// index.js
const readline = require('readline');

// Create an interface for reading input from the console
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Get the current date and time
const now = new Date();

// Ask the user for their name
rl.question('What is your name? ', (name) => {
  // Display the greeting and current date and time
  console.log(`Hello, ${name}! The current date and time is ${now.toString()}.`);
  
  // Close the readline interface
  rl.close();
});
```

#### Running the Project
```bash
node index.js
```

#### Code Breakdown
1. **Import readline module**: Enables console input/output
2. **Create interface**: Sets up stdin/stdout communication
3. **Get current date**: Creates a Date object for timestamp
4. **Ask question**: Prompts user for input with callback
5. **Display result**: Shows greeting with user's name and timestamp
6. **Close interface**: Properly terminates the program

## Async Logic & Project Setup
<chapterId>c605916f-4a5e-4c2c-ac4d-8e556f454012</chapterId>

### Understanding Node.js Under the Hood

#### The Event Loop
The event loop is Node.js's secret weapon for handling multiple operations efficiently:

##### Key Concepts
- **Single-threaded**: Node.js executes one task at a time
- **Non-blocking**: Doesn't get stuck waiting for slow operations
- **Event-driven**: Responds to events as they occur
- **Callback queue**: Manages tasks waiting to be executed

##### How It Works
1. Node.js receives a task
2. If the task is quick, it executes immediately
3. If the task is slow (file reading, network request), it:
   - Starts the task
   - Registers a callback function
   - Moves to the next task
   - Executes the callback when the slow task completes

#### Asynchronous Operations
**Asynchronous** means "not at the same time":
- **Synchronous**: Like a phone call - both parties must be present
- **Asynchronous**: Like text messaging - responses come when convenient

##### Callbacks
Callbacks are functions that run after another function completes:
```javascript
// Reading a file asynchronously
fs.readFile('data.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data); // This runs AFTER the file is read
});

console.log('This runs BEFORE the file is read');
```

### Setting Up Your First Node.js Project

#### Step 1: Installation
1. Visit [nodejs.org](https://nodejs.org)
2. Download the LTS version for your operating system
3. Run the installer and follow the prompts
4. Verify installation:
```bash
node --version
npm --version
```

#### Step 2: Create Your Project
```bash
# Create project directory
mkdir hello-node
cd hello-node

## Initialize Node.js project
npm init -y

## Create main file
touch index.js  # or create in your code editor
```

#### Step 3: Your First Node.js Code
```javascript
// index.js
console.log("Hello, Node.js!");
```

#### Step 4: Run Your Code
```bash
node index.js
```

### Best Practices for Node.js Development

#### 1. Project Organization
- Use descriptive file and folder names
- Keep related files together
- Separate concerns into different modules
- Create a logical project structure

#### 2. Error Handling
- Always handle errors in callbacks
- Use try-catch blocks for synchronous code
- Provide meaningful error messages

#### 3. Code Quality
- Write clear, readable code
- Use consistent naming conventions
- Comment complex logic
- Keep functions small and focused

#### Common Issues and Solutions

#### 1. "Module not found" Error
**Problem**: `Error: Cannot find module 'module-name'`
**Solution**: 
```bash
npm install module-name
```

#### 2. "node: command not found"
**Problem**: Node.js not installed properly
**Solution**: 
- Reinstall Node.js from official website
- Check PATH environment variable
- Restart terminal

#### 3. Permission Errors
**Problem**: Cannot install packages globally
**Solution**: 
```bash
## Use npx for one-time use
npx package-name

## Or configure npm properly
npm config set prefix '~/.npm-global'
```

#### Exercise: Build Your First Node.js App

#### Challenge
Create a simple calculator app that:
1. Asks the user for two numbers
2. Asks for an operation (+, -, *, /)
3. Displays the result

#### Starter Code
```javascript
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Your code here
```

#### Solution Approach
1. Use nested readline questions
2. Convert strings to numbers
3. Use a switch statement for operations
4. Handle division by zero
5. Close the interface properly

### Additional Resources and Next Steps of Node Js

#### Documentation
- [Node.js Official Documentation](https://nodejs.org/en/docs/)
- [NPM Documentation](https://docs.npmjs.com/)
- [CommonJS Modules](https://nodejs.org/api/modules.html)

#### Learning Resources
- [Node.js Crash Course](https://www.youtube.com/watch?v=fBNz5xF-Kx4) - 1-hour video tutorial
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices) - GitHub repository
- [Node.js Basics Cheat Sheet](https://overapi.com/nodejs) - Quick reference

#### Development Tools
- [Nodemon](https://nodemon.io/) - Auto-restart server during development
- [Node.js Debugger](https://nodejs.org/en/docs/guides/debugging-getting-started/) - Built-in debugging tools


#### Immediate Actions
1. **Set up Node.js** on your development machine
2. **Complete the mini project** from this lesson
3. **Experiment** with different built-in modules
4. **Practice** the require/module.exports pattern

#### Prepare for Lesson 2
In our next lesson, we'll dive into building our first server using Express.js. We'll cover:
- Setting up an Express server
- Creating routes and endpoints
- Handling HTTP requests and responses
- Building the foundation for our Lightning Wallet backend

#### Key Takeaways
- Node.js is just JavaScript in a different environment
- The event loop makes Node.js fast and efficient
- Modules help organize and share code
- NPM provides access to millions of packages
- Asynchronous programming is fundamental to Node.js

#### Remember
Every expert was once a beginner. Node.js might seem overwhelming at first, but it's built on JavaScript fundamentals you already know. Focus on understanding the concepts, practice regularly, and don't be afraid to experiment.

The journey from frontend to full-stack developer starts with this single step. You're not just learning Node.js – you're building the foundation for creating powerful, scalable applications that can handle real-world traffic and solve real problems.

Ready to build your first server? Let's continue to Lesson 2! 🚀 

# Building APIs with Express
<partId>159cb08d-a0de-4259-94cb-a5c7df238ac1</partId>

## Express Server Basics 
<chapterId>dabebb1d-26a3-4101-bd6b-8d7a67e3b746</chapterId>

![Video](https://peertube.planb.network/videos/embed/c6369582-8c03-46d8-80f6-de859990a197)

### Understanding HTTP APIs

#### Definition
An **HTTP API** (Application Programming Interface) is a web-based interface that allows communication between different systems or applications over the internet using the HTTP protocol.

#### Breaking Down the Acronym
- **HTTP**: Hypertext Transfer Protocol - the fundamental protocol of the internet
- **API**: Application Programming Interface - the "interface" is the key word here

Think of an API as a **contract** or **gateway** between your secure server environment and the outside world. It defines exactly:
- What data clients can request
- What data clients can send
- How that communication happens
- What responses they'll receive

#### Why HTTP APIs Matter

##### Security and Control
- **Server-side protection**: Your business logic and sensitive data stay secure
- **Controlled access**: You define exactly what operations are allowed
- **Data validation**: You can validate and sanitize all incoming data
- **Authentication**: You control who can access what resources

##### Standardization
- **Universal protocol**: HTTP works across all platforms and devices
- **Consistent patterns**: RESTful APIs follow established conventions
- **Interoperability**: Different systems can communicate seamlessly

#### The Client-Server Model
The API facilitates communication in the **client-server model**:

| Client Side | Server Side |
|-------------|-------------|
| Makes requests | Handles requests |
| Displays data | Stores and processes data |
| User interactions | Business logic |
| Potentially insecure | Secure environment |

### HTTP Methods and CRUD Operations

#### Understanding CRUD
**CRUD** represents the four basic operations you can perform on data:

- **C**reate - Add new data
- **R**ead - Retrieve existing data  
- **U**pdate - Modify existing data
- **D**elete - Remove data

#### HTTP Methods Map to CRUD

| HTTP Method | CRUD Operation | Purpose | Example |
|-------------|----------------|---------|---------|
| `POST` | Create | Add new resource | Create new user |
| `GET` | Read | Retrieve data | Get user profile |
| `PUT` | Update | Replace entire resource | Update user info |
| `DELETE` | Delete | Remove resource | Delete user account |

#### RESTful API Design
**REST** (Representational State Transfer) is a set of architectural principles:

```
GET    /users          # Get all users
GET    /users/123      # Get user with ID 123
POST   /users          # Create new user
PUT    /users/123      # Update user with ID 123
DELETE /users/123      # Delete user with ID 123
```

### Setting Up Your Express.js Environment

#### Step 1: Project Initialization
```bash
## Create project directory
mkdir pleb-wallet-backend
cd pleb-wallet-backend

## Initialize Node.js project
npm init -y

## Create main server file
touch index.js

## Install Express
npm install express
```

#### Step 2: Project Structure
After setup, your project should look like this:
```
pleb-wallet-backend/
├── index.js
├── package.json
├── package-lock.json
└── node_modules/
```

#### Understanding package.json
```json
{
  "name": "pleb-wallet-backend",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

### Building Your First Express Server

#### Complete Server Code
```javascript
// index.js

// Import the Express library
const express = require("express");

// Create a new instance of the Express server
const server = express();

// Use the built-in JSON middleware to parse incoming JSON requests
server.use(express.json());

// Set up a route to handle GET requests to the root path
server.get("/", (req, res) => {
  // Send a JSON response with a "message" property set to "I'm alive!"
  res.status(200).json({ message: "I'm alive!" });
});

// Set the server to listen on the provided port, or 5500 if no port is specified
const PORT = process.env.PORT || 5500;

server.listen(PORT, () => {
  // Log a message to the console when the server starts listening
  console.log(`Server listening on port ${PORT}`);
});
```

#### Code Breakdown

##### 1. Import Express
```javascript
const express = require("express");
```
- Uses CommonJS module system to import Express
- Express is now available as a function

##### 2. Create Server Instance
```javascript
const server = express();
```
- Calls `express()` to create a new application instance
- This instance will handle all HTTP requests

##### 3. Configure Middleware
```javascript
server.use(express.json());
```
- **Middleware** runs between receiving a request and sending a response
- `express.json()` parses incoming JSON data from request bodies
- Essential for handling POST/PUT requests with JSON data

##### 4. Define Route/Endpoint
```javascript
server.get("/", (req, res) => {
  res.status(200).json({ message: "I'm alive!" });
});
```
- `server.get()` defines a route that responds to GET requests
- `"/"` is the **endpoint** or **route path**
- `(req, res)` are the request and response objects
- `res.status(200)` sets HTTP status code to 200 (OK)
- `res.json()` sends a JSON response

##### 5. Start Server
```javascript
const PORT = process.env.PORT || 5500;
server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```
- `process.env.PORT` checks for environment variable (useful for deployment)
- Falls back to port 5500 for local development
- `server.listen()` starts the server
- Callback function runs when server is ready

## Requests, Responses & Testing
<chapterId>3d95cc16-925c-47ff-9177-f96bf218b31a</chapterId>

### Understanding Request and Response Objects

#### The Request Object (req)
The `req` object contains information about the incoming HTTP request:

```javascript
server.get("/users", (req, res) => {
  // Request properties you can access:
  console.log(req.method);     // HTTP method (GET, POST, etc.)
  console.log(req.url);        // Full URL path
  console.log(req.headers);    // HTTP headers
  console.log(req.query);      // Query string parameters
  console.log(req.params);     // URL parameters
  console.log(req.body);       // Request body (for POST/PUT)
});
```

#### The Response Object (res)
The `res` object is used to send responses back to the client:

```javascript
server.get("/users", (req, res) => {
  // Different ways to send responses:
  res.status(200).json({ users: [] });           // JSON response
  res.status(201).send("User created");          // Text response
  res.status(404).json({ error: "Not found" });  // Error response
  res.redirect("/login");                         // Redirect
});
```

### HTTP Status Codes

#### Common Status Codes
Understanding status codes is crucial for API development:

| Code | Status | When to Use |
|------|--------|-------------|
| 200 | OK | Successful GET, PUT, DELETE |
| 201 | Created | Successful POST (resource created) |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource doesn't exist |
| 500 | Internal Server Error | Server-side error |

#### Status Code Examples
```javascript
// Success responses
res.status(200).json({ message: "Success" });
res.status(201).json({ id: 123, message: "User created" });

// Error responses  
res.status(400).json({ error: "Invalid input" });
res.status(404).json({ error: "User not found" });
res.status(500).json({ error: "Server error" });
```

### Testing Your API (Insomnia/Postman)

#### Using Insomnia or Postman

##### Installation
1. Download [Insomnia](https://insomnia.rest/) (recommended) or [Postman](https://www.postman.com/)
2. Install and create a new project
3. Both are free and provide excellent API testing capabilities

##### Making Your First API Request
1. **Start your server**: `node index.js`
2. **Open Insomnia**
3. **Create new request**:
   - Method: GET
   - URL: `http://localhost:5500`
   - Click Send

##### Expected Response
```json
{
  "message": "I'm alive!"
}
```

#### Testing Different Endpoints
```javascript
// Add more endpoints to test
server.get("/users", (req, res) => {
  res.status(200).json({ 
    users: [
      { id: 1, name: "Alice" },
      { id: 2, name: "Bob" }
    ]
  });
});

server.post("/users", (req, res) => {
  const { name } = req.body;
  res.status(201).json({ 
    id: Date.now(), 
    name: name,
    message: "User created successfully" 
  });
});
```

### Building Multiple Endpoints

#### Expanding Your API
Let's create a more comprehensive API structure:

```javascript
// index.js - Enhanced version
const express = require("express");
const server = express();

// Middleware
server.use(express.json());

// Root endpoint
server.get("/", (req, res) => {
  res.status(200).json({ message: "Lightning Wallet API is alive!" });
});

// Users endpoints
server.get("/users", (req, res) => {
  // In a real app, this would come from a database
  const users = [
    { id: 1, username: "alice", email: "alice@example.com" },
    { id: 2, username: "bob", email: "bob@example.com" }
  ];
  res.status(200).json({ users });
});

server.get("/users/:id", (req, res) => {
  const { id } = req.params;
  // In a real app, query the database
  const user = { id: parseInt(id), username: "alice", email: "alice@example.com" };
  res.status(200).json({ user });
});

server.post("/users", (req, res) => {
  const { username, email } = req.body;
  
  // Validate input
  if (!username || !email) {
    return res.status(400).json({ error: "Username and email are required" });
  }
  
  // In a real app, save to database
  const newUser = {
    id: Date.now(),
    username,
    email,
    createdAt: new Date().toISOString()
  };
  
  res.status(201).json({ user: newUser, message: "User created successfully" });
});

// Lightning endpoints (placeholder for future lessons)
server.get("/lightning/info", (req, res) => {
  res.status(200).json({ 
    message: "Lightning integration coming soon!",
    nodeId: "placeholder"
  });
});

// Error handling middleware
server.use((req, res) => {
  res.status(404).json({ error: "Endpoint not found" });
});

const PORT = process.env.PORT || 5500;
server.listen(PORT, () => {
  console.log(`🚀 Lightning Wallet Backend listening on port ${PORT}`);
});
```

## Building Your Express.js Server 
<chapterId>90b9132e-8f1a-4012-a6e7-c5572c2d1a58</chapterId>

### Best Practices for Express Development

#### 1. Project Organization
```
pleb-wallet-backend/
├── index.js              # Main server file
├── routes/               # Route definitions
│   ├── userRoutes.js
│   └── lightningRoutes.js
├── middleware/           # Custom middleware
│   └── auth.js
├── models/              # Data models
│   └── User.js
├── utils/               # Utility functions
│   └── validation.js
├── package.json
└── .env                 # Environment variables
```

#### 2. Error Handling
```javascript
// Always handle errors properly
server.get("/users/:id", (req, res) => {
  try {
    const { id } = req.params;
    
    // Validate input
    if (!id || isNaN(id)) {
      return res.status(400).json({ error: "Invalid user ID" });
    }
    
    // Process request
    const user = getUserById(id);
    
    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }
    
    res.status(200).json({ user });
  } catch (error) {
    console.error("Error getting user:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});
```

#### 3. Input Validation
```javascript
const validateUser = (userData) => {
  const errors = [];
  
  if (!userData.username || userData.username.length < 3) {
    errors.push("Username must be at least 3 characters");
  }
  
  if (!userData.email || !userData.email.includes("@")) {
    errors.push("Valid email is required");
  }
  
  return errors;
};

server.post("/users", (req, res) => {
  const errors = validateUser(req.body);
  
  if (errors.length > 0) {
    return res.status(400).json({ errors });
  }
  
  // Process valid data
});
```

#### Common Issues and Solutions

#### 1. Port Already in Use
**Problem**: `Error: listen EADDRINUSE :::5500`
**Solution**: 
```bash
## Kill process using the port
lsof -ti:5500 | xargs kill -9

## Or use a different port
const PORT = process.env.PORT || 5501;
```

#### 2. Cannot POST/PUT Data
**Problem**: Request body is undefined
**Solution**: 
```javascript
// Make sure you have JSON middleware
server.use(express.json());

// For form data, also add:
server.use(express.urlencoded({ extended: true }));
```

#### 3. CORS Issues
**Problem**: Frontend can't access your API
**Solution**: 
```bash
npm install cors
```
```javascript
const cors = require('cors');
server.use(cors());
```

### Hands-on Exercise: Build a Task API

#### Challenge
Create a simple task management API with the following endpoints:
- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `GET /tasks/:id` - Get a specific task
- `PUT /tasks/:id` - Update a task
- `DELETE /tasks/:id` - Delete a task

#### Starter Code
```javascript
const express = require("express");
const server = express();

server.use(express.json());

// In-memory storage (replace with database later)
let tasks = [
  { id: 1, title: "Learn Node.js", completed: false },
  { id: 2, title: "Build Express API", completed: false }
];

// Your endpoints here

const PORT = process.env.PORT || 5500;
server.listen(PORT, () => {
  console.log(`Task API listening on port ${PORT}`);
});
```

#### Solution Framework
```javascript
// GET all tasks
server.get("/tasks", (req, res) => {
  res.status(200).json({ tasks });
});

// POST new task
server.post("/tasks", (req, res) => {
  const { title } = req.body;
  // Validate and create task
  // Return 201 status with new task
});

// GET specific task
server.get("/tasks/:id", (req, res) => {
  const { id } = req.params;
  // Find task by ID
  // Return 404 if not found
});

// PUT update task
server.put("/tasks/:id", (req, res) => {
  const { id } = req.params;
  // Update task
  // Return updated task
});

// DELETE task
server.delete("/tasks/:id", (req, res) => {
  const { id } = req.params;
  // Remove task from array
  // Return 204 status
});
```


### Environment Variables and Configuration

#### Using .env Files
```bash
## Install dotenv
npm install dotenv
```

Create `.env` file:
```
PORT=5500
NODE_ENV=development
DATABASE_URL=your_database_url
```

Load in your application:
```javascript
require('dotenv').config();

const PORT = process.env.PORT || 5500;
const NODE_ENV = process.env.NODE_ENV || 'development';
```

### Development Workflow Improvements

#### Auto-restart with Nodemon
```bash
## Install nodemon for development
npm install -g nodemon

## Or install locally
npm install --save-dev nodemon
```

Add to `package.json`:
```json
{
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  }
}
```

Run with auto-restart:
```bash
npm run dev
```

### API Documentation Best Practices

#### Document Your Endpoints
```javascript
/**
 * @route GET /users
 * @desc Get all users
 * @access Public
 * @returns {Array} Array of user objects
 */
server.get("/users", (req, res) => {
  // Implementation
});

/**
 * @route POST /users
 * @desc Create a new user
 * @access Public
 * @param {String} username - User's username
 * @param {String} email - User's email
 * @returns {Object} Created user object
 */
server.post("/users", (req, res) => {
  // Implementation
});
```


#### What's Coming Next
In Lesson 3, we'll dive deeper into:
- Advanced routing with Express Router
- Database integration with SQL
- User authentication and authorization
- Middleware patterns and security
- Error handling strategies

#### Immediate Actions
1. **Complete the hands-on exercise** - Build the task API
2. **Experiment with different endpoints** - Try POST, PUT, DELETE
3. **Test with Insomnia/Postman** - Get comfortable with API testing
4. **Set up nodemon** - Improve your development workflow

#### Key Takeaways
- Express.js makes server development straightforward and powerful
- HTTP APIs follow RESTful conventions for consistency
- Request/response objects provide all the data you need
- Status codes communicate the outcome of operations
- Middleware provides a powerful way to extend functionality
- Proper error handling is essential for robust APIs

#### Official Documentation
- [Express.js Official Documentation](https://expressjs.com/)
- [Node.js HTTP Module](https://nodejs.org/api/http.html)
- [MDN HTTP Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

#### Learning Resources
- [Express.js Crash Course](https://www.youtube.com/watch?v=L72fhGm1tfE) - YouTube tutorial
- [REST API Design Best Practices](https://restfulapi.net/) - Comprehensive guide
- [Express.js Cheatsheet](https://devhints.io/express) - Quick reference

#### Development Tools
- [Insomnia](https://insomnia.rest/) - API testing tool
- [Postman](https://www.postman.com/) - Alternative API testing
- [Nodemon](https://nodemon.io/) - Development server auto-restart

#### Summary

Congratulations! You've just built your first Express.js server and learned the fundamentals of HTTP API development. You now understand:

- How to create and configure Express servers
- The principles of RESTful API design
- HTTP methods and status codes
- Request/response handling
- API testing with dedicated tools
- Best practices for server development

This foundation is crucial for everything we'll build in the rest of the course. In our next lesson, we'll expand on these concepts by adding database integration and user authentication to create a more sophisticated backend system.

The journey from understanding Node.js to building production-ready APIs is well underway. You're not just learning Express.js - you're mastering the patterns and practices that power modern web applications.

Ready to add a database to your server? Let's continue to Lesson 3! 🚀 


## Modular Routing
<chapterId>11c569de-ecee-4dec-9bff-a45f60fe038f</chapterId>

### Express Router Concepts

#### REST APIs
**REST** (Representational State Transfer) is a widely adopted philosophy for building APIs that can communicate in a structured way. Think of REST as a common language that developers use to build API routes and endpoints.

REST provides standard methods:
- **GET**: Retrieve data
- **POST**: Create new data
- **PUT**: Update existing data
- **DELETE**: Remove data

#### Express Router
Express Router is a built-in middleware function that allows you to:
- Group and organize routes into separate files
- Keep code modular and organized
- Make applications easier to maintain and scale
- Define multiple routes with specific URL patterns and HTTP methods

### Planning Our API Structure

Before we start coding, let's plan what our pleb-wallet-backend needs:

#### Data Categories
1. **Users**
   - Signup/authentication flows
   - Admin rights for wallet spending
   - Authorized users can create invoices
   - Non-logged-in users can view balance only

2. **Lightning**
   - Create invoices (authenticated users)
   - Pay invoices (admin only)
   - Get wallet balance (anyone)
   - Save/retrieve paid and received invoices

#### API Routes Structure

##### Root Route
```
GET / - Welcome message
```

##### Users Routes (`/users`)
```
GET /users - Get all users
POST /users/register - Register a new user
POST /users/login - Login existing user
PUT /users/:id - Update user by ID
DELETE /users/:id - Delete user by ID
GET /users/user - Get user by username
```

##### Lightning Routes (`/lightning`)
```
GET /lightning/invoices - Get all invoices
POST /lightning/invoice - Create an invoice
POST /lightning/pay - Pay an invoice
GET /lightning/balance - Get wallet balance
```

### Implementation

#### Step 1: Create Router Files

First, create the routers folder and files:

```bash
mkdir routers
touch routers/usersRouter.js
touch routers/lightningRouter.js
```

Your project structure should now look like this:
```
pleb-wallet-backend/
├── routers/
│   ├── usersRouter.js
│   └── lightningRouter.js
├── index.js
├── package.json
└── ...
```

#### Step 2: Build Users Router

Create `routers/usersRouter.js`:

```javascript
const router = require("express").Router();

// GET all users
router.get("/", (req, res) => {
  res.status(200).json({ message: "I'm alive!" });
});

// GET user by their username
router.get("/user", (req, res) => {
  res.status(200).json({ message: "I'm alive!" });
});

// POST a user to register
router.post("/register", (req, res) => {
  const user = req.body;
  
  console.log(user);
  
  res.status(201).json({ message: "I'm alive!" });
});

// POST a user to login
router.post("/login", (req, res) => {
  const user = req.body;
  
  console.log(user);
  
  res.status(200).json({ message: "I'm alive!" });
});

// PUT a user to update them by their id
router.put("/:id", (req, res) => {
  const id = req.params.id;
  const user = req.body;
  
  console.log(id, user);
  
  res.status(200).json({ message: "I'm alive!" });
});

// DELETE a user by their id
router.delete("/:id", (req, res) => {
  const id = req.params.id;
  
  console.log(id);
  
  res.status(200).json({ message: "I'm alive!" });
});

// Export our router so we can use it in index.js
module.exports = router;
```

#### Step 3: Build Lightning Router

Create `routers/lightningRouter.js`:

```javascript
const router = require("express").Router();

// GET lightning wallet balance
router.get("/balance", (req, res) => {
  res.status(200).json({ message: "I'm alive!" });
});

// GET all invoices from the database
router.get("/invoices", (req, res) => {
  res.status(200).json({ message: "I'm alive!" });
});

// POST required info to create an invoice
router.post("/invoice", (req, res) => {
  const { value, memo } = req.body;
  
  console.log(value, memo);
  
  res.status(200).json({ message: "I'm alive!" });
});

// POST an invoice to pay
router.post("/pay", (req, res) => {
  const { payment_request } = req.body;
  
  console.log(payment_request);
  
  res.status(200).json({ message: "I'm alive!" });
});

// Export our router so we can use it in index.js
module.exports = router;
```

#### Step 4: Update index.js

Add the router imports and middleware to your `index.js`:

```javascript
const express = require("express");
const usersRouter = require("./routers/usersRouter");
const lightningRouter = require("./routers/lightningRouter");

// Create a new instance of the Express server
const server = express();

// Use the built-in JSON middleware to parse incoming JSON requests
server.use(express.json());

// Set up a route to handle GET requests to the root path
server.get("/", (req, res) => {
  // Send a JSON response with a "message" property set to "I'm alive!"
  res.status(200).json({ message: "I'm alive!" });
});

// Add our routers before server.listen()
server.use("/users", usersRouter);
server.use("/lightning", lightningRouter);

// Set the server to listen on the provided port, or 5500 if no port is specified
const PORT = process.env.PORT || 5500;

server.listen(PORT, () => {
  // Log a message to the console when the server starts listening
  console.log(`Server listening on port ${PORT}`);
});
```

### Understanding Request Parameters

Express allows you to define routes with parameters using a colon (`:`) followed by the parameter name.

```javascript
// Route with parameter
router.get("/:id", (req, res) => {
  const id = req.params.id; // Extract the id from the URL
  // Handle the request...
});
```

Examples:
- `/users/123` - id would be "123"
- `/users/john-doe` - id would be "john-doe"

#### Testing Your API

#### Start Your Server
```bash
node index.js
```

#### Test Endpoints with Insomnia

Set up the following requests in Insomnia:

##### GET Requests
- `GET http://localhost:5500/` - Root endpoint
- `GET http://localhost:5500/users` - Get all users
- `GET http://localhost:5500/users/user` - Get user by username
- `GET http://localhost:5500/lightning/invoices` - Get all invoices
- `GET http://localhost:5500/lightning/balance` - Get wallet balance

##### POST Requests with JSON Body

**Register User:**
```
POST http://localhost:5500/users/register
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```

**Login User:**
```
POST http://localhost:5500/users/login
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```

**Create Invoice:**
```
POST http://localhost:5500/lightning/invoice
Content-Type: application/json

{
  "value": 1000,
  "memo": "Test invoice"
}
```

**Pay Invoice:**
```
POST http://localhost:5500/lightning/pay
Content-Type: application/json

{
  "payment_request": "lnbc1000n1..."
}
```

##### PUT/DELETE Requests with Parameters

**Update User:**
```
PUT http://localhost:5500/users/3
Content-Type: application/json

{
  "username": "updateduser"
}
```

**Delete User:**
```
DELETE http://localhost:5500/users/1
```

### Key Takeaways and Resources

#### Express Router Benefits
- **Modular Organization**: Keep related routes together
- **Maintainability**: Easy to find and update specific functionality
- **Scalability**: Add new features without cluttering main file
- **Reusability**: Share middleware and handlers across routes

#### RESTful Design Principles
- Use appropriate HTTP methods for different operations
- Structure URLs to represent resources logically
- Maintain consistent naming conventions
- Keep endpoints predictable and intuitive

#### DRY Principle
**Don't Repeat Yourself** - By organizing code into routers, we avoid duplicating logic and create reusable components.


#### Resources

- [Express Routing Official Documentation](https://expressjs.com/en/guide/routing.html)
- [Express Router Tutorial](https://scotch.io/tutorials/learn-to-use-the-new-router-in-expressjs-4)
- [RESTful Routing in Express](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/routes#RESTful_routing_in_Express)
- [REST APIs: How They Work](https://blog.hubspot.com/website/what-is-rest-api)
- [Express Request Parameters](https://www.educative.io/answers/what-is-reqparams-in-expressjs)

#### Review

In this lesson, we covered:

1. **Express Routers**: How to create and use routers to organize routes for specific parts of our application
2. **RESTful APIs**: Creating a standardized interface for interacting with application resources using HTTP methods
3. **Request Parameters**: Handling dynamic parameters in Express routes for flexible endpoint design
4. **API Testing**: Using Insomnia to test our endpoints and verify functionality

We now have a solid foundation for our pleb-wallet-backend with organized, testable endpoints ready for the next phase of development! 



## Lesson 4: Express Middleware Logic
<chapterId>07e08ea3-904a-44c0-a7ed-4cdac8c2dc98</chapterId>


### What is Middleware?

Middleware is a function that sits between the request and response objects and can modify or intercept either one before they reach their destination. Think of it as a series of checkpoints that every request passes through before reaching your endpoint logic.

#### Key Characteristics

- **Sits in the middle**: Between request and response in the request-response cycle
- **Can modify data**: Transform requests or responses
- **Can terminate cycles**: Send responses or pass control to next middleware
- **Order matters**: Executed in the order they're defined

#### Common Use Cases

- **Authentication**: Verify user identity and permissions
- **Logging**: Track incoming requests and outgoing responses
- **Error Handling**: Catch and handle errors gracefully
- **Compression**: Reduce response size for better performance
- **CORS**: Enable cross-origin requests
- **Rate Limiting**: Prevent abuse and DoS attacks
- **Caching**: Store frequently requested data
- **CSRF Protection**: Prevent cross-site request forgery
- **Custom Functionality**: Add any custom logic to your request pipeline

---

### How Express Middleware Works

Middleware functions are functions that have access to the request object, response object, and the next middleware function in the application's request-response cycle.

#### Middleware Function Structure

```javascript
app.use((req, res, next) => {
  // Your middleware logic here
  next(); // Pass control to next middleware
});
```

#### Parameters

- **`req`**: The request object containing client data
- **`res`**: The response object for sending data back
- **`next`**: Function that passes control to the next middleware

#### Example: Multiple Middleware Functions

```javascript
// Middleware function 1
app.use((req, res, next) => {
  console.log('Middleware 1');
  next(); // Pass control to next middleware
});

// Middleware function 2  
app.use((req, res, next) => {
  console.log('Middleware 2');
  res.send('Hello World!'); // Terminates the cycle
});

// Middleware function 3
app.use((req, res, next) => {
  console.log('Middleware 3');
  // This won't execute - previous middleware sent response
});
```

---

#### Built-in Middleware
```javascript
// JSON parsing middleware
server.use(express.json());

// URL-encoded form data
server.use(express.urlencoded({ extended: true }));

// Serve static files
server.use(express.static('public'));
```

#### Custom Middleware
```javascript
// Logging middleware
const logger = (req, res, next) => {
  console.log(`${req.method} ${req.url} - ${new Date().toISOString()}`);
  next(); // Pass control to next middleware
};

server.use(logger);

// Authentication middleware (coming in later lessons)
const authenticate = (req, res, next) => {
  // Check for valid token
  const token = req.headers.authorization;
  
  if (!token) {
    return res.status(401).json({ error: "No token provided" });
  }
  
  // Verify token logic here
  next();
};

// Use on specific routes
server.get("/protected", authenticate, (req, res) => {
  res.json({ message: "You are authenticated!" });
});
```


### Setting Up Middleware in Our Pleb Wallet Backend

#### Step 1: Install Middleware Packages

First, let's install the essential middleware packages we'll be using:

```bash
npm install helmet morgan cors express-rate-limit
```

#### The Middleware We're Adding

##### 🛡️ Helmet
- **Purpose**: Security enhancement through HTTP headers
- **Protection**: XSS attacks, clickjacking, and other common vulnerabilities
- **Implementation**: Sets various security-related HTTP headers

##### 📝 Morgan
- **Purpose**: HTTP request/response logging
- **Benefits**: Debugging, monitoring, and analytics
- **Formats**: Multiple logging formats available

##### 🌐 CORS
- **Purpose**: Cross-Origin Resource Sharing
- **Function**: Allows web pages from different domains to access your API
- **Security**: Configurable access controls

##### ⚡ Express-Rate-Limit
- **Purpose**: Rate limiting to prevent abuse
- **Protection**: DoS attacks, brute-force attempts
- **Configuration**: Customizable limits per IP address

#### Step 2: Import Middleware

Update your `index.js` file with the new imports:

```javascript
const express = require("express");
const helmet = require("helmet");
const morgan = require("morgan");
const cors = require("cors");
const rateLimit = require("express-rate-limit");
const usersRouter = require("./routers/usersRouter");
const lightningRouter = require("./routers/lightningRouter");
```

#### Step 3: Initialize Basic Middleware

Add these middleware functions **before** `server.use(express.json())`:

```javascript
// Create Express server instance
const server = express();

// Security middleware - sets various HTTP headers
server.use(helmet());

// Logging middleware - logs all requests in 'common' format
server.use(morgan("common"));

// CORS middleware - enables cross-origin requests
server.use(cors());
```

#### Step 4: Add Rate Limiting

```javascript
// Rate limiting middleware - prevents abuse
server.use(
  rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
  })
);
```

#### Complete Updated index.js

```javascript
const express = require("express");
const helmet = require("helmet");
const morgan = require("morgan");
const cors = require("cors");
const rateLimit = require("express-rate-limit");
const usersRouter = require("./routers/usersRouter");
const lightningRouter = require("./routers/lightningRouter");

const server = express();

// Security middleware
server.use(helmet());

// Logging middleware
server.use(morgan("common"));

// CORS middleware
server.use(cors());

// Rate limiting middleware
server.use(
  rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
  })
);

// JSON parsing middleware
server.use(express.json());

// Routes
server.get("/", (req, res) => {
  res.status(200).json({ message: "I'm alive!" });
});

server.use("/users", usersRouter);
server.use("/lightning", lightningRouter);

const PORT = process.env.PORT || 5500;

server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```

---

## Security & Development Tools
<chapterId>594cecd2-38a4-4cb3-a6f5-e0080e824463</chapterId>

### Development Tool: Nodemon

#### What is Nodemon?

Nodemon is a utility that automatically restarts your Node.js server whenever file changes are detected. This saves you from manually stopping and starting your server during development.

#### Installation

```bash
npm install nodemon
```

#### Setup

Update your `package.json` scripts:

```json
{
  "name": "pleb-wallet-backend",
  "version": "1.0.0",
  "description": "Lightning wallet backend for PlebDevs course",
  "main": "index.js",
  "scripts": {
    "start": "nodemon index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2",
    "helmet": "^6.0.1",
    "morgan": "^1.10.0",
    "cors": "^2.8.5",
    "express-rate-limit": "^6.7.0"
  }
}
```

#### Usage

Start your server with automatic restart capability:

```bash
npm run start
```

You should see output similar to:
```
[nodemon] 2.0.20
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node index.js`
Server listening on port 5500
```

---

### Testing Your Middleware

#### 1. Testing Morgan (Logging)

Make a request to your server using any HTTP client (browser, Postman, etc.):

```
GET http://localhost:5500/
```

You should see log output in your terminal:
```
::1 - - [23/Mar/2024:10:30:45 +0000] "GET / HTTP/1.1" 200 24
```

This shows:
- IP address
- Timestamp
- HTTP method and path
- Status code
- Response size

#### 2. Testing Helmet (Security Headers)

Check the response headers from your last request. You should see additional security headers like:
- `X-XSS-Protection`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Strict-Transport-Security`

#### 3. Testing CORS

CORS will allow cross-origin requests. You can test this by making requests from different domains or using fetch from a browser console on a different website.

---

### Understanding Denial of Service (DoS) Attacks

#### What is a DoS Attack?

A Denial of Service attack attempts to overwhelm a server with traffic, making it unavailable to legitimate users. Common methods include:

- **Request Flooding**: Sending high volumes of requests
- **Resource Exhaustion**: Consuming server resources
- **Bandwidth Consumption**: Filling network capacity

#### The Pattern

Many cyber attacks follow a simple pattern: **repetitive or looping behavior**. Attackers use automated tools to repeatedly perform actions, often just a simple for loop!

#### Our Defense: Rate Limiting

Rate limiting protects against these attacks by:
- Limiting requests per IP address
- Setting time windows for request limits
- Automatically blocking excessive requests

---


Let's test our rate limiting by performing a controlled attack on our own server!

#### The Attack Script

```javascript
const http = require('http');

function sendRequest() {
  const options = {
    host: 'localhost',
    port: 5500,
    path: '/',
    method: 'GET',
  };

  const req = http.request(options, (res) => {
    console.log(`Response status code: ${res.statusCode}`);
  });

  req.on('error', (e) => {
    console.error(`Request error: ${e.message}`);
  });

  req.end();
}

// Send a request every 100ms
setInterval(sendRequest, 100);
```

#### Running the Attack

1. **Start your server** (if not already running):
   ```bash
   npm run start
   ```

2. **Open a new terminal** and enter Node.js REPL:
   ```bash
   node
   ```

3. **Paste the attack script** and press Enter

4. **Watch the magic happen**:
   - You'll see status codes start as `200` (success)
   - After 100 requests, they'll switch to `429` (rate limited)
   - Your server logs will show all the requests via Morgan

5. **Stop the attack** with `Ctrl+C`

#### What You Should See

```
Response status code: 200
Response status code: 200
Response status code: 200
...
Response status code: 429
Response status code: 429
Response status code: 429
```

The `429` status code means "Too Many Requests" - your rate limiting is working!

---

### Key Takeaways about Middleware and Resources

#### Middleware Concepts
- **Functions between request and response**: Middleware sits in the request-response cycle
- **Order matters**: Middleware executes in the order it's defined
- **Can terminate or continue**: Either send a response or call `next()`
- **Modular functionality**: Each middleware handles a specific concern

#### Security Benefits
- **Helmet**: Adds security headers to prevent common attacks
- **Rate Limiting**: Prevents abuse and DoS attacks
- **CORS**: Controls cross-origin access
- **Logging**: Provides visibility into server activity

#### Development Improvements
- **Nodemon**: Automatic server restarts during development
- **Better debugging**: Comprehensive logging with Morgan
- **Security by default**: Protection against common vulnerabilities

---

#### What's Next?

In the next lesson, we'll dive deeper into custom middleware by building our own authentication middleware. We'll learn how to:

- Create custom middleware functions
- Implement JWT-based authentication
- Protect routes with authentication middleware
- Handle authentication errors gracefully

---

#### Resources

#### Official Documentation
- [Express Middleware Guide](https://expressjs.com/en/guide/using-middleware.html)
- [Helmet.js Documentation](https://helmetjs.github.io/)
- [Morgan Documentation](https://github.com/expressjs/morgan)
- [CORS Documentation](https://github.com/expressjs/cors)

#### Additional Learning
- [Express.js Middleware Tutorial](https://www.tutorialspoint.com/expressjs/expressjs_middleware.htm)
- [Express.js Fundamentals - Middleware Explained](https://www.youtube.com/watch?v=9HOem0amlyg)
- [Security Best Practices](https://expressjs.com/en/advanced/best-practice-security.html)

---


#### Common Issues

**Server won't start after adding middleware:**
- Check that all packages are installed: `npm install`
- Verify middleware is added before routes
- Ensure proper syntax in middleware setup

**Rate limiting not working:**
- Verify the rate limit configuration
- Check that requests are coming from the same IP
- Ensure rate limiting middleware is before other middleware

**Headers not showing security additions:**
- Confirm Helmet is installed and configured
- Check that Helmet middleware is being used
- Verify in browser dev tools or HTTP client

**Nodemon not restarting:**
- Check that the script is correctly configured in package.json
- Verify file changes are being saved
- Try manually restarting with `rs` in the terminal

---

*Great job completing Lesson 4! You've successfully enhanced your server with essential middleware for security, logging, and development efficiency. Your Pleb Wallet backend is becoming more robust and production-ready with each lesson.* 


## JWT Authentication & Hashing
<chapterId>00d42dd7-4cf2-4f3e-a358-c12e020fd05b</chapterId>


### Authentication Basics & JSON Web Tokens (JWT)

Authentication is the process of verifying the identity (or pseudo-identity) of a user or system accessing your server. In web applications, authentication is crucial for:

- **Protecting sensitive resources** - Database, Lightning node, user data
- **Controlling access** - Who can do what in your application
- **Maintaining security** - Preventing unauthorized actions

> 🔒 **Security First**: Without proper authentication, anyone could potentially access your sensitive information or perform actions on your behalf.

---

#### What are JWTs?

JSON Web Tokens are an open standard (RFC 7519) for securely transmitting information between parties as a JSON object. They're perfect for authentication because they are:

- **Stateless** - No server-side storage required
- **Scalable** - Easy to distribute across multiple servers
- **Self-contained** - Carry all necessary information

#### JWT Structure

A JWT consists of three parts separated by dots (`.`):

```
header.payload.signature
```

1. **Header** - Specifies the algorithm used (e.g., HS256)
2. **Payload** - Contains user data and claims
3. **Signature** - Verifies the token's authenticity

#### JWT Debugger

Visit [jwt.io](https://jwt.io) to visualize and debug JWT tokens. This tool is invaluable for understanding JWT structure and troubleshooting authentication issues.

---

### Setting Up JWT Authentication

#### Step 1: Install Required Packages

```bash
npm install jsonwebtoken bcryptjs dotenv
```

- **jsonwebtoken** - JWT creation and verification
- **bcryptjs** - Password hashing
- **dotenv** - Environment variable management

#### Step 2: Import Dependencies

Add these imports to your `usersRouter.js`:

```javascript
const jwt = require("jsonwebtoken");
const bcrypt = require("bcryptjs");
```

#### Step 3: Create Token Generation Function

Add this function to the bottom of your `usersRouter.js`:

```javascript
/**
 * Generate a JSON Web Token (JWT) for a given user
 * @param {Object} user - User object containing id, username, admin status
 * @returns {string} - Signed JWT token
 */
function generateToken(user) {
  // Define the payload to be included in the token
  const payload = {
    id: user.id,
    username: user.username,
    admin: user.admin,
  };
  
  // Get the JWT secret from environment variables
  const secret = process.env.JWT_SECRET || "Satoshi Nakamoto";
  
  // Define token options
  const options = {
    expiresIn: "1d", // Token expires in 1 day
  };
  
  // Generate and return the JWT
  return jwt.sign(payload, secret, options);
}
```

---

### Environment Variables

#### Why Use Environment Variables?

Environment variables allow you to:
- **Store sensitive data** separate from your code
- **Enable different configurations** for development/production
- **Prevent secrets** from being committed to version control

#### Setting Up Environment Variables

1. **Create a `.env` file** in your project root:

```bash
## Server configuration
PORT=5500

## JWT Secret (use a strong, random string in production)
JWT_SECRET=keepitsecretkeepitsafe

## Admin key for elevated permissions
ADMIN_KEY=1234
```

2. **Create/Update `.gitignore`**:

```
node_modules/
.env
```

> ⚠️ **Important**: Never commit your `.env` file to version control!

3. **Install and configure dotenv** in `index.js`:

```javascript
const dotenv = require("dotenv");

// Load environment variables
dotenv.config();

// Use environment variables
const PORT = process.env.PORT || 5500;
```

---

### Password Hashing with bcryptjs

#### Why Hash Passwords?

- **Security** - Plain text passwords are vulnerable if your database is compromised
- **One-way function** - Hashes cannot be reversed to reveal the original password
- **Comparison** - bcrypt can compare plain text passwords to hashed versions

#### Hashing Process

```javascript
// Hash a password
const hashedPassword = bcrypt.hashSync(password, 14);

// Compare passwords
const isValid = bcrypt.compareSync(plainTextPassword, hashedPassword);
```

#### Updated Login Endpoint

Replace your existing login endpoint in `usersRouter.js`:

```javascript
router.post("/login", (req, res) => {
  // Extract credentials from request body
  const { username, password } = req.body;
  
  // Placeholder user object (will be replaced with database query)
  const DBuser = {
    username: "test",
    password: "pass1",
  };
  
  // Hash the stored password for comparison
  const hashedPassword = bcrypt.hashSync(DBuser.password, 14);
  
  // Verify user credentials
  if (DBuser && bcrypt.compareSync(password, hashedPassword)) {
    // Generate JWT token
    const token = generateToken(DBuser);
    
    // Send success response
    res.status(200).json({ 
      message: `Welcome ${DBuser.username}!`, 
      token, 
      DBuser 
    });
  } else {
    // Send error response
    res.status(401).json({ message: "Invalid credentials" });
  }
});
```

---

## Authorization & Route Protection
<chapterId>5c45a258-9270-42a1-815c-7e8c35816c88</chapterId>

### Custom Authentication Middleware

#### Planning Our Access Levels

Our application will have three levels of access:

1. **Public** - Anyone can view wallet balance and transactions
2. **Authenticated Users** - Can create invoices
3. **Admin Users** - Can pay invoices (spend money!)

#### Creating the Middleware Directory

Create the following structure:
```
routers/
  middleware/
    authenticate.js
    authenticateAdmin.js
```

#### Basic Authentication Middleware

Create `routers/middleware/authenticate.js`:

```javascript
const jwt = require("jsonwebtoken");

/**
 * Middleware to authenticate users via JWT
 * Checks for valid JWT token in Authorization header
 */
module.exports = (req, res, next) => {
  // Extract token from Authorization header
  const token = req.headers.authorization;
  
  // Get JWT secret from environment variables
  const secret = process.env.JWT_SECRET || "Satoshi Nakamoto";
  
  if (token) {
    // Verify the token
    jwt.verify(token, secret, (err, decodedToken) => {
      if (err) {
        // Token is invalid
        res.status(401).json({ 
          message: "Not Allowed", 
          Error: err.message 
        });
      } else {
        // Token is valid, continue to next middleware/endpoint
        console.log("Decoded token:", decodedToken);
        next();
      }
    });
  } else {
    // No token provided
    res.status(401).json({ message: "No token!" });
  }
};
```

#### Admin Authentication Middleware

Create `routers/middleware/authenticateAdmin.js`:

```javascript
const jwt = require("jsonwebtoken");

/**
 * Middleware to authenticate admin users
 * Checks for valid JWT token AND admin key
 */
module.exports = (req, res, next) => {
  // Extract token from Authorization header
  const token = req.headers.authorization;
  
  // Get JWT secret from environment variables
  const secret = process.env.JWT_SECRET || "Satoshi Nakamoto";
  
  if (token) {
    jwt.verify(token, secret, async (err, decodedToken) => {
      if (err || !decodedToken) {
        // Token verification failed
        res.status(401).json({ 
          message: "Error with your verification" 
        });
      } else {
        // Token is valid, now check admin privileges
        
        // Placeholder user object (will be replaced with database query)
        const user = {
          username: "test",
          password: "pass1",
          adminKey: 1234,
        };
        
        // Extract admin key from user object
        const adminKey = user?.adminKey?.toString() ?? "";
        
        // Check if user has valid admin key
        if (adminKey !== process.env.ADMIN_KEY) {
          // User is not an admin
          res.status(401).json({ message: "Must be an admin" });
        } else {
          // User is admin, continue to endpoint
          next();
        }
      }
    });
  } else {
    // No token provided
    res.status(401).json({ message: "No token!" });
  }
};
```

---

### Implementing Middleware on Endpoints

#### Protecting the Create Invoice Endpoint

Update your `lightningRouter.js`:

```javascript
const authenticate = require("./middleware/authenticate");

// POST endpoint to create an invoice (requires authentication)
router.post("/invoice", authenticate, (req, res) => {
  const { value, memo } = req.body;
  
  console.log("Creating invoice:", { value, memo });
  
  res.status(200).json({ message: "I'm alive!" });
});
```

#### Protecting the Pay Invoice Endpoint

```javascript
const authenticateAdmin = require("./middleware/authenticateAdmin");

// POST endpoint to pay an invoice (requires admin privileges)
router.post("/pay", authenticateAdmin, (req, res) => {
  const { payment_request } = req.body;
  
  console.log("Paying invoice:", payment_request);
  
  res.status(200).json({ message: "I'm alive!" });
});
```

---

### Testing Your Authentication System

#### Test 1: Unauthenticated Request

Try accessing the protected endpoint without a token:

```bash
## Should return 401 - No token!
curl -X POST http://localhost:5500/lightning/invoice
```

#### Test 2: Get Authentication Token

Login to get a JWT token:

```bash
curl -X POST http://localhost:5500/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "test", "password": "pass1"}'
```

#### Test 3: Authenticated Request

Use the token from step 2 in the Authorization header:

```bash
curl -X POST http://localhost:5500/lightning/invoice \
  -H "Authorization: YOUR_JWT_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"value": 1000, "memo": "Test invoice"}'
```

#### Test 4: Admin Request

Test the admin endpoint with the same token:

```bash
curl -X POST http://localhost:5500/lightning/pay \
  -H "Authorization: YOUR_JWT_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"payment_request": "lnbc..."}'
```

---

#### Common HTTP Status Codes

Understanding these status codes is crucial for authentication:

- **200 OK** - Request successful
- **401 Unauthorized** - Authentication failed
- **403 Forbidden** - Authenticated but not authorized
- **500 Internal Server Error** - Server-side error

---

#### Security Best Practices

##### 1. Strong JWT Secrets
```javascript
// BAD - Predictable secret
JWT_SECRET=password123

// GOOD - Random, long secret
JWT_SECRET=h8f9d7s6f5g4h3j2k1l0m9n8b7v6c5x4z3a2s1d0f9g8h7j6k5l4m3n2b1v0c9x8z7
```

##### 2. Token Expiration
```javascript
const options = {
  expiresIn: "1d", // Tokens expire in 1 day
};
```

##### 3. Environment Variables
- Never commit `.env` files to version control
- Use different secrets for different environments
- Rotate secrets regularly in production

##### 4. Password Hashing
```javascript
// Use appropriate salt rounds (12-15 for production)
const hashedPassword = bcrypt.hashSync(password, 14);
```

---

#### Troubleshooting Common Issues

#### Issue: "Invalid signature" error
**Cause**: Token was signed with a different secret
**Solution**: Ensure the same JWT_SECRET is used for signing and verification

#### Issue: "Token expired" error
**Cause**: JWT has passed its expiration time
**Solution**: User needs to login again to get a new token

#### Issue: "No token" error
**Cause**: Authorization header is missing or incorrectly formatted
**Solution**: Ensure the header is set as `Authorization: your-jwt-token`

#### Issue: "Must be an admin" error
**Cause**: User doesn't have admin privileges
**Solution**: Verify the user has the correct adminKey in their profile

---

### Last Steps about Authentication

1. **Authentication is Critical** - Never skip security in your applications
2. **JWTs are Stateless** - Perfect for scalable applications
3. **Environment Variables** - Keep secrets separate from code
4. **Middleware is Powerful** - Use it to implement cross-cutting concerns
5. **Defense in Depth** - Use multiple layers of security

---

#### Additional Resources

- [JWT.io](https://jwt.io/) - JWT debugger and documentation
- [bcryptjs npm package](https://www.npmjs.com/package/bcryptjs) - Password hashing library
- [dotenv npm package](https://www.npmjs.com/package/dotenv) - Environment variable management
- [Express Middleware Guide](https://expressjs.com/en/guide/using-middleware.html) - Official Express middleware documentation

---

#### Practice Exercises

1. **Create a logout endpoint** that invalidates tokens (hint: you'll need to maintain a blacklist)
2. **Add token refresh functionality** to extend user sessions
3. **Implement role-based access control** with different user roles
4. **Add rate limiting** to prevent brute force attacks on login

> 💡 **Remember**: This is one of the most complex lessons in the course. Take your time, experiment with the code, and don't hesitate to review the concepts multiple times. Authentication is a fundamental skill that you'll use in every backend application you build.

#### Additional Resources

- [JWT.io](https://jwt.io/) - JWT debugger and documentation
- [bcryptjs npm package](https://www.npmjs.com/package/bcryptjs) - Password hashing library
- [dotenv npm package](https://www.npmjs.com/package/dotenv) - Environment variable management
- [Express Middleware Guide](https://expressjs.com/en/guide/using-middleware.html) - Official Express middleware documentation

---

# Entering into the Ligthning Network Layer
<partId>4e7d3c30-07b7-4ddb-91cc-77a6d3f107ec</partId>

## Introduction to the Protocol
<chapterId>44ffb7e7-252c-454b-8458-0aa35917526d</chapterId>

### The Lightning Network

The Lightning Network is a **second-layer solution** built on top of Bitcoin's blockchain that enables faster and more scalable transactions.

**Key Concepts:**

##### Second Layer
- Built on top of Bitcoin without changing the protocol
- Extends Bitcoin's capabilities using clever trade-offs
- Uses Bitcoin's inherent features in innovative ways
- Different from sidechains or hard forks

##### Off-Chain Transactions
- Enables payments between users without recording every transaction on the blockchain
- Reduces the load on the main Bitcoin blockchain
- Transactions happen "off-chain" but are still secured by Bitcoin

##### Micropayments
- Allows for small, instant transactions with minimal fees
- Expands the range of possible Bitcoin use cases significantly
- Makes Bitcoin practical for everyday transactions

### Lightning Nodes

#### What are Lightning Nodes?

Lightning nodes are **network participants** - computers that participate in the Lightning Network by running compatible software.

**Think of them as servers that:**
- Receive requests
- Process them
- Send responses
- But in the context of Lightning payments

#### Key Functions

##### Routing Payments
- Nodes help route transactions through the network
- Forward payments between channels
- Payments literally pass through nodes on the network
- Much more active role than Bitcoin nodes

##### Decentralization
- Large number of nodes ensures network remains decentralized
- Resistant to censorship or control by single entities
- Multiple routing paths provide redundancy
- If one node goes down, payments can route through others

### Lightning Channels

#### Understanding Payment Channels

Payment channels are **temporary, private channels** between users that allow for multiple transactions without requiring on-chain confirmations.

#### Channel Structure

##### Multi-Signature Wallets
- Each channel is essentially a 2-of-2 multisig wallet
- Both parties have control over funds
- Both parties must agree on every payment
- Ensures security and trust

##### Directional Nature
- **Important:** Channels are unidirectional!
- When you open a channel, all funds start on your side
- To send money, liquidity shifts from your side to theirs
- For bidirectional payments, both parties need to open channels

##### Network of Channels
- Users can route payments through multiple channels
- Don't need direct channels with every recipient
- Payments hop through multiple nodes to reach destination

#### Visual Example

```
Alice ----[Channel]----> Bob ----[Channel]----> Carol

Alice can pay Carol even without a direct channel!
```

### Lightning Network Architecture

#### Network Layers

```
┌─────────────────────────────────────────────┐
│           Application Layer                 │
│        (Your Lightning App)                │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│           Lightning Layer                   │
│      (Lightning Network Nodes)             │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│            Bitcoin Layer                    │
│         (Bitcoin Core Node)                │
└─────────────────────────────────────────────┘
```

#### Node Communication Types

1. **Bitcoin Core Connection** (Required)
   - Lightning nodes need Bitcoin blockchain data
   - Every Lightning node connects to Bitcoin Core
   - Provides chain data and transaction information

2. **Peer Connections** (Gossip)
   - Lightning nodes talk to each other
   - Share network updates and channel information
   - Bidirectional communication for network awareness

3. **Payment Channels** (Business)
   - Actual channels for moving money
   - Built on top of peer connections
   - Where the real Lightning magic happens

## Development Environment
<chapterId>ee2416e8-6c3c-4c41-a571-16822a14a5bc</chapterId>

### Lightning Implementations

#### What is a Lightning Implementation?

A Lightning implementation is a **software package** that:
- Implements the Lightning specification
- Allows nodes to participate in the Lightning Network
- Provides necessary functionalities for a Lightning node

#### The Lightning Spec

- There's a detailed specification that all implementations must follow
- Ensures compatibility between different implementations
- Still evolving and being developed
- Very complex protocol with multiple layers

#### Popular Implementations

##### LND (Lightning Network Daemon)
- **Developer:** Lightning Labs
- **Language:** Go
- **Status:** Most popular and widely used
- **Features:** 
  - Rich feature set
  - Extensive documentation
  - Great developer experience
  - Excellent API

##### Core Lightning
- **Developer:** Blockstream
- **Language:** C
- **Features:**
  - Optimized for performance and reliability
  - Flexible plugin system
  - Feature-rich
  - Easy to extend with Python scripts

##### Eclair
- **Developer:** ACINQ
- **Language:** Scala
- **Features:**
  - Highly scalable
  - User-friendly wallet app
  - Mobile SDK for app development
  - Enterprise-level features
  - Powers Phoenix wallet

##### LDK (Lightning Development Kit)
- **Developer:** Spiral (formerly Square Crypto)
- **Language:** Rust
- **Features:**
  - Modular, customizable toolkit
  - Safety and performance focused
  - For building custom Lightning implementations
  - Great for wallet integration

##### Other Implementations
- **Electrum:** Smaller implementation, can run on mobile
- Various other experimental implementations

### Protocol vs Application Development

#### Understanding the Layers

```
┌─────────────────────────────────────────────┐
│         Frontend Development               │
│    (UI/UX, Mobile, Web Interfaces)        │
│         PlebDevs Course #1                 │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│        Backend Development                 │
│   (Application Server, API, Business)     │
│         PlebDevs Course #2                 │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│        Protocol Development                │
│  (Lightning Node, Bitcoin Node Software)  │
│         Advanced/Specialized               │
└─────────────────────────────────────────────┘
```

#### Development Philosophy

##### Protocol Development
- **Approach:** Move slow and fix things
- **Focus:** Reliability, security, consensus
- **Complexity:** Very high
- **Examples:** Building LND, Core Lightning, Bitcoin Core

##### Application Development
- **Approach:** Move fast and break things (with care for users' money!)
- **Focus:** User experience, features, iteration
- **Complexity:** Moderate
- **Examples:** Lightning wallets, payment apps

#### Our Focus: Application Development

In this course, we're **application developers** building on top of the Lightning protocol:
- We don't need to understand every protocol detail
- We use existing Lightning implementations (LND)
- We focus on user experience and business logic
- We naturally learn protocol concepts as we build

### Setting Up Local Lightning Development Environment

#### Required Tools

##### Docker Desktop
- **Purpose:** Containerized development environment
- **Why:** Isolates Lightning software from your system
- **Download:** [Docker Desktop](https://www.docker.com/products/docker-desktop)

##### Polar
- **Purpose:** Local Lightning Network simulator
- **Why:** Test Lightning functionality without real money
- **Website:** [polarlightning.com](https://polarlightning.com)

#### Setting Up Polar

##### 1. Install Prerequisites
```bash
# Install Docker Desktop first
# Then install Polar from the website
```

##### 2. Create Your First Network
1. Open Polar
2. Click "Create Network"
3. Name your network (e.g., "Pleb Wallet BE")
4. Choose node implementations:
   - Bitcoin Core: 1 (required)
   - LND: 3 (recommended for learning)
   - Core Lightning: 0
   - Eclair: 0
5. Click "Create"

##### 3. Start Your Network
1. Click "Start" button
2. Wait for all nodes to turn green
3. You now have a local Lightning Network!

#### Understanding RegTest

Your Polar network runs on **RegTest**:
- **RegTest:** Local and fake Bitcoin network
- **TestNet:** Global and fake Bitcoin network  
- **MainNet:** Global and real Bitcoin network

**Benefits of RegTest:**
- Completely local (no internet required)
- Instant block generation
- Free "fake" Bitcoin for testing
- Safe environment to experiment

#### Basic Polar Operations

##### Adding Funds
1. Click on any node (e.g., Alice)
2. Go to "Actions" tab
3. Click "Deposit" → "1M sats"
4. Watch block height increase automatically

##### Opening Channels
1. Click "Open Channel" on funded node
2. Select "Outgoing" for one-directional channel
3. Choose destination node
4. Set channel amount
5. Click "Open Channel"

##### Making Payments
1. Have recipient create invoice
2. Copy invoice from recipient node
3. Go to sender node
4. Click "Pay Invoice"
5. Paste invoice and send
6. Watch channel liquidity shift visually!

#### Channel Liquidity Visualization

Polar shows channel liquidity with colors:
- **Green:** Your liquidity (can send)
- **Blue:** Remote liquidity (can receive)
- **Mixed:** Balanced channel

As you send payments, watch the colors shift - this represents the movement of satoshis within the channel!

### Key Takeaways About Lightning Network

1. **Lightning is a Second Layer:** Built on Bitcoin, not changing it
2. **Nodes Route Payments:** Your payment may hop through multiple nodes
3. **Channels are Directional:** Need liquidity on your side to send
4. **Multiple Implementations:** LND, Core Lightning, Eclair, LDK all work together
5. **App vs Protocol:** We're building apps, not the protocol itself
6. **Polar is Essential:** Perfect tool for Lightning development and learning


#### Essential Reading
- [Lightning Network White Paper](https://lightning.network/lightning-network-paper.pdf)
- [Mastering the Lightning Network Book (Free)](https://github.com/lnbook/lnbook)

#### Video Resources
- [Bitcoin's Lightning Network, Simply Explained!](https://www.youtube.com/watch?v=rrr_zPmEiME)
- [A Technical Introduction to The Lightning Network](https://www.youtube.com/watch?v=E1n3sKKPD_k&t=330s)
- [Lightning Series: Mastering Lightning with Andreas M. Antonopoulos & René Pickhardt](https://www.youtube.com/watch?v=zG8PZsHLung)

#### Technical Resources
- [Understanding the Lightning Network (Bitcoin Magazine Series)](https://bitcoinmagazine.com/technical/understanding-the-lightning-network-part-building-a-bidirectional-payment-channel-1464710791)
- [Polar Lightning](https://polarlightning.com)
- [LND Documentation](https://docs.lightning.engineering/)

#### Practice Exercises

1. **Set up Polar** with at least 3 LND nodes
2. **Create channels** between all nodes
3. **Make payments** and watch liquidity shift
4. **Try routing** payments through multiple hops
5. **Experiment** with different channel amounts and configurations

Remember: This is a safe environment to break things and learn! Try force-closing channels, routing through multiple nodes, and getting familiar with Lightning concepts before we start building our application. 

## Building on LND
<chapterId>54143d9f-bb41-4874-bba4-2474e565da6f</chapterId>


**Note:** This is a hands-on coding lesson where we'll move real (fake) money with our own code!

### What is a Lightning App?

A Lightning App is just like any other application but with Lightning added. However, this opens up many architectural decisions:

#### Key Questions to Consider

When building a Lightning app, you need to decide:

1. **Node Management**
   - Does your app need a dedicated node?
   - Will you use a Lightning Service Provider (LSP)?
   - Will users run their own nodes?

2. **Wallet Custody**
   - Will users get a custodial wallet from you?
   - Will they connect their own wallet?
   - Will they get a non-custodial wallet?
   - Will they even know they're using Lightning?

3. **User Experience**
   - How much Lightning complexity do you expose?
   - What trade-offs will you make for ease of use?

#### Our Architecture

For the Pleb Wallet, we're building:
- **One hosted node** (Alice in our Polar setup)
- **Multiple users** interacting with our wallet
- **Custodial setup** where only we (admins) can spend
- **Users can create invoices** and receive payments

### Typical Full Stack Lightning App Architecture

```
┌─────────────────────────────────────────────┐
│                Frontend                     │
│        (User Interface & Experience)       │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│                   API                       │
│    (HTTP Communication Layer)               │
│  • GET, POST, UPDATE, DELETE                │
│  • Call Lightning node methods              │
│  • Handle authentication                    │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│                Database                     │
│     (Optional - App Data Storage)           │
│  • User data                               │
│  • Invoice records                         │
│  • Payment history                         │
└─────────────────────────────────────────────┘
                        ↕
┌─────────────────────────────────────────────┐
│            Lightning Node                   │
│    (Wallet, Network Node, Payment DB)      │
│  • Manages Bitcoin/Lightning funds          │
│  • Connects to Lightning Network            │
│  • Processes payments                       │
└─────────────────────────────────────────────┘
```

### Common Lightning Development Hurdles

#### 1. Running a Node
- **Challenge:** Hosting, maintaining, and keeping nodes operational
- **Solutions:** 
  - Voltage (managed Lightning infrastructure)
  - Umbrel (self-hosted solution)

#### 2. Talking to Your Node
- **Challenge:** Understanding how to communicate with Lightning nodes
- **Solutions:**
  - gRPC wrappers (LND-GRPC, ln-service)
  - Pre-built interfaces (LNBits, RTL, WebLN, LNC)

#### 3. Development Environment
- **Challenge:** Safe environment for testing without real money
- **Solutions:**
  - Polar (what we're using)
  - Workbench (CLI alternative)

#### 4. Getting Liquidity
- **Challenge:** Opening channels and managing Lightning liquidity
- **Solutions:**
  - FLOW by Voltage
  - Magma by Amboss

### Understanding gRPC

#### What is gRPC?

**gRPC** stands for "gRPC Remote Procedure Calls" - a modern, high-performance framework for machine-to-machine communication.

##### Key Features:
- **Binary Protocol:** More efficient than JSON/HTTP
- **Strongly Typed:** Reduces errors and ensures consistency
- **Streaming Support:** Real-time data pipelines
- **Multi-Language:** Works with JavaScript, Python, Go, etc.
- **Connection Persistence:** No request/response handshake needed

##### gRPC vs HTTP Comparison:

| Feature | HTTP/REST | gRPC |
|---------|-----------|------|
| Data Format | JSON (text) | Protocol Buffers (binary) |
| Connection | Request/Response | Persistent streaming |
| Real-time | Requires polling | Native streaming |
| Performance | Good | Excellent |
| Complexity | Simple | Moderate |

#### Benefits of gRPC Wrapper Libraries

Instead of writing raw gRPC code like this:
```javascript
// Raw gRPC - 40+ lines just to call getInfo!
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
// ... 35+ more lines of boilerplate ...
client.getInfo(request, (err, response) => {
  console.log(response);
});
```

We can use LND-GRPC wrapper:
```javascript
// With LND-GRPC wrapper - simple and clean!
const info = await lnd.services.Lightning.getInfo();
```
## Integrating LND with Code
<chapterId>5273d1b7-6940-41eb-8147-f38cc8e7448c</chapterId>

### Setting Up LND Connection

#### Step 1: Get Connection Credentials

From your Polar Alice node, go to the **Connect** tab and gather:

1. **HOST:** gRPC Host (e.g., `127.0.0.1:10001`)
2. **CERT:** TLS Cert File Path
3. **MACAROON:** Admin Macaroon File Path

#### Step 2: Add to Environment Variables

Add these to your `.env` file:
```env
# Lightning node connection
HOST=127.0.0.1:10001
CERT=/path/to/your/tls.cert
MACAROON=/path/to/your/admin.macaroon
```

**Security Note:** These credentials provide full admin access to your node. Never commit them to version control!

#### Step 3: Install LND-GRPC

```bash
npm install lnd-grpc
```

#### Step 4: Create LND Connection File

Create `lnd.js` in your project root:

```javascript
const LndGrpc = require("lnd-grpc");
const dotenv = require("dotenv");

dotenv.config();

const options = {
  host: process.env.HOST,
  cert: process.env.CERT,
  macaroon: process.env.MACAROON,
};

const lnd = new LndGrpc(options);

const connect = async () => {
  try {
    await lnd.connect();

    if (lnd.state !== "active") {
      throw new Error(
        "LND did not reach 'active' state within the expected time"
      );
    }

    console.log(`LND gRPC connection state: ${lnd.state}`);
  } catch (e) {
    console.log("error", e);
  }
};

module.exports = { connect };
```

#### Step 5: Connect on Server Startup

In your `index.js`, add the connection:

```javascript
const { connect } = require("./lnd");

// ... other middleware ...
server.use(express.json());

// Connect to our LND node
connect();
```

### Building LND Methods

#### Balance Methods

Add these methods to your `lnd.js`:

```javascript
/**
 * Get the on-chain Bitcoin balance
 * @returns {Promise<Object>} Wallet balance information
 */
const getBalance = async () => {
  const balance = await lnd.services.Lightning.walletBalance();
  return balance;
};

/**
 * Get the Lightning channel balance
 * @returns {Promise<Object>} Channel balance information
 */
const getChannelBalance = async () => {
  const channelBalance = await lnd.services.Lightning.channelBalance();
  return channelBalance;
};

module.exports = {
  connect,
  getBalance,
  getChannelBalance,
};
```

#### Invoice Creation Method

```javascript
/**
 * Create a Lightning invoice
 * @param {number} value - Amount in satoshis
 * @param {string} memo - Invoice description
 * @returns {Promise<Object>} Invoice object with payment_request
 */
const createInvoice = async ({ value, memo }) => {
  const invoice = await lnd.services.Lightning.addInvoice({
    value: value,
    memo: memo,
  });

  // TODO: Save invoice to database
  
  return invoice;
};
```

#### Payment Method

```javascript
/**
 * Pay a Lightning invoice
 * @param {string} payment_request - Lightning invoice to pay
 * @returns {Promise<Object>} Payment result
 */
const payInvoice = async ({ payment_request }) => {
  const paidInvoice = await lnd.services.Lightning.sendPaymentSync({
    payment_request: payment_request,
  });

  return paidInvoice;
};
```

### Real-Time Invoice Updates with Event Streams

#### Understanding Event Streams

Event streams provide real-time updates without polling:

- **Traditional Polling:** Ask "Is my invoice paid?" every second
- **Event Streams:** Get notified instantly when invoice is paid

#### Implementing Invoice Event Stream

```javascript
/**
 * Subscribe to invoice events for real-time updates
 * Listens for when invoices are created, paid, or expire
 */
const invoiceEventStream = async () => {
  await lnd.services.Lightning.subscribeInvoices({
    add_index: 0,    // Start from beginning of invoice history
    settle_index: 0, // Start from beginning of settlement history
  })
    .on("data", async (data) => {
      if (data.settled) {
        console.log("Invoice settled:", data);
        
        // Check if invoice exists in database
        const existingInvoice = false; // TODO: Check database
        
        if (existingInvoice) {
          // TODO: Update invoice status in database
          console.log("Updating invoice in database");
        } else {
          console.log("Invoice not found in database");
        }
      }
    })
    .on("error", (err) => {
      console.error("Invoice stream error:", err);
    });
};
```

#### Start Event Stream on Connection

Update your `connect` function:

```javascript
const connect = async () => {
  try {
    await lnd.connect();

    if (lnd.state !== "active") {
      throw new Error(
        "LND did not reach 'active' state within the expected time"
      );
    }

    // Start the invoice event stream
    invoiceEventStream();

    console.log(`LND gRPC connection state: ${lnd.state}`);
  } catch (e) {
    console.log("error", e);
  }
};
```

### Adding Lightning Routes & Testing

#### Import LND Methods

In your `lightningRouter.js`:

```javascript
const {
  getBalance,
  createInvoice,
  getChannelBalance,
  payInvoice,
} = require("../lnd.js");
```

#### Balance Endpoints

```javascript
// GET the on-chain balance
router.get("/balance", (req, res) => {
  getBalance()
    .then((balance) => {
      res.status(200).json(balance);
    })
    .catch((err) => {
      res.status(500).json(err);
    });
});

// GET the Lightning channel balance
router.get("/channelbalance", (req, res) => {
  getChannelBalance()
    .then((channelBalance) => {
      res.status(200).json(channelBalance);
    })
    .catch((err) => {
      res.status(500).json(err);
    });
});
```

#### Invoice Endpoints

```javascript
// POST - Create a new invoice
router.post("/invoice", authenticate, (req, res) => {
  const { value, memo } = req.body;

  createInvoice({ value, memo })
    .then((invoice) => {
      res.status(200).json(invoice);
    })
    .catch((err) => {
      res.status(500).json(err);
    });
});

// POST - Pay an invoice (admin only)
router.post("/pay", authenticateAdmin, async (req, res) => {
  const { payment_request } = req.body;

  try {
    const pay = await payInvoice({ payment_request });

    if (pay.payment_error) {
      return res.status(500).json(pay.payment_error);
    }

    if (pay?.payment_route) {
      // TODO: Save successful payment to database
      res.status(200).json(pay);
    }
  } catch (err) {
    res.status(500).json(err);
  }
});
```

#### Testing Your Lightning Integration Using Insomnia/Postman

1. **Start your server** and ensure Polar network is running
2. **Login** to get a JWT token
3. **Test Balance Endpoints:**
   - GET `/lightning/balance`
   - GET `/lightning/channelbalance`

4. **Test Invoice Creation:**
   - POST `/lightning/invoice`
   - Body: `{ "value": 1000, "memo": "Test invoice" }`

5. **Test Payment:**
   - Create invoice in Polar (Bob creates invoice)
   - POST `/lightning/pay`
   - Body: `{ "payment_request": "lnbc..." }`

#### Understanding Balance Types

- **On-chain Balance:** Bitcoin sitting on the blockchain
- **Channel Balance:** 
  - `local_balance`: Sats you can send
  - `remote_balance`: Sats you can receive

#### Troubleshooting Common Issues

1. **Connection Failed**
   - Check Polar network is running
   - Verify credentials in `.env`
   - Check file paths are correct

2. **Invoice Creation Fails**
   - Ensure you're authenticated
   - Check value is a number
   - Verify memo is a string

3. **Payment Fails**
   - Check you have channel balance
   - Verify invoice is valid
   - Ensure route exists between nodes

### Key Takeaways about Integrating LND

1. **gRPC is Powerful:** Enables real-time communication with Lightning nodes
2. **Wrapper Libraries Help:** LND-GRPC reduces complexity significantly
3. **Event Streams Are Essential:** Real-time updates without polling
4. **Security Matters:** Macaroons provide fine-grained access control
5. **Testing is Key:** Use Polar for safe development environment


#### Practice Exercises

1. **Explore the LND API:** Browse the [LND documentation](https://lightning.engineering/api-docs/) and try calling different methods
2. **Create Multiple Invoices:** Test creating invoices with different values and memos
3. **Test Payment Routes:** Create invoices on different nodes and pay them
4. **Monitor Event Streams:** Watch the console logs when invoices are paid
5. **Experiment with Channels:** Open new channels in Polar and test routing

#### Essential Reading
- [LND gRPC Documentation](https://lightning.engineering/api-docs/)
- [LND-GRPC NPM Package](https://www.npmjs.com/package/lnd-grpc)
- [Protocol Buffers Documentation](https://developers.google.com/protocol-buffers)

#### Video Resources
- [Build Bitcoin into Your App: Getting Started with the Lightning Network](https://www.youtube.com/watch?v=6P0DZ74DmFA)
- [LND Overview and Developer Guide](https://dev.lightning.community/overview/)

#### Development Tools
- [Polar Lightning](https://polarlightning.com) - Local Lightning development
- [Voltage](https://voltage.cloud) - Managed Lightning infrastructure
- [Insomnia](https://insomnia.rest) - API testing tool

#### Lightning Development Resources
- [Lightning Labs Build Your First LAPP](https://docs.lightning.engineering/lapps/guides/polar-lapps)
- [A crash course in Lightning App Development](https://medium.com/@rheedio/a-crash-course-in-lightning-app-development-5be5b8d2d558)
- [Express / React Lightning app template](https://github.com/AustinKelsay/pleb-node-template)

Remember: This is just the beginning! Lightning development opens up incredible possibilities for micropayments, instant settlements, and innovative financial applications. Take your time to understand these concepts - they're the foundation for everything we'll build going forward. 

# Managing Relational Databases & SQL
<partId>3266da0c-6d0f-4e90-824f-27631ad30836</partId>

## Introduction to Databases
<chapterId>61114e89-8587-48b8-8376-dba352b0914b</chapterId>

**Note:** This is a foundational lesson that will prepare us for hands-on database development in the next lessons!

### What is a Database?

A database is a collection of data that is organized in a specific way to make it easily accessible and manageable. Think of it as a sophisticated filing system for your application's data.

#### Key Characteristics

**Organized Structure:** Data is stored in a structured manner that allows for efficient searching, sorting, and querying. This organization is what makes databases powerful compared to storing data in simple files.

**Accessibility:** Databases provide standardized ways to access data, whether you're searching for a specific user, sorting transactions by date, or querying for complex relationships between data points.

**Scalability:** As your application grows from hundreds to thousands to millions of users, databases are designed to handle this growth efficiently.

#### Types of Data

Databases can store many different types of data:
- **Text:** User names, descriptions, messages
- **Numbers:** Amounts, IDs, timestamps
- **Binary Data:** Images, videos, files
- **Structured Data:** JSON objects, arrays

For our Lightning wallet application, we'll primarily work with text and numbers, but understanding the full scope helps you make informed decisions for future projects.

#### Types of Databases

Understanding different database types is crucial for choosing the right tool for your project. Each type is optimized for different use cases and comes with its own trade-offs.

#### 1. Relational Databases

**Most Common Choice:** When people say "database," they often mean relational databases. These are the industry standard for most applications.

##### How They Work:
- **Tables:** Data is stored in tables with rows and columns
- **Rows:** Each row represents a single record (like one user)
- **Columns:** Each column represents an attribute (like username or email)
- **Relationships:** Tables can be connected through shared keys

##### Key Benefits:
- **Data Integrity:** Strong constraints ensure data consistency
- **ACID Properties:** Atomicity, Consistency, Isolation, Durability
- **Mature Ecosystem:** Decades of development and optimization
- **SQL Standard:** Universal query language

##### Common Examples:
- **MySQL:** Most popular open-source database
- **PostgreSQL:** Advanced features, great for complex queries
- **SQLite:** Lightweight, perfect for development
- **Oracle:** Enterprise-grade, feature-rich

#### 2. Document-Oriented Databases

**Flexible Structure:** These databases store data as documents, usually in JSON or XML format.

##### How They Work:
- **Documents:** Each record is a document with nested data
- **Collections:** Groups of similar documents
- **Flexible Schema:** Structure can vary between documents

##### Key Benefits:
- **Rapid Development:** Easy to get started and iterate
- **Flexible Schema:** No need to define structure upfront
- **Natural JSON:** Works seamlessly with JavaScript applications

##### Trade-offs:
- **Scaling Challenges:** Can become problematic at scale
- **Loose Constraints:** Easier to introduce data inconsistencies
- **Query Limitations:** Complex relationships are harder to manage

##### Common Examples:
- **MongoDB:** Most popular document database
- **CouchDB:** Built for distributed systems

#### 3. Key-Value Stores

**Simple and Fast:** These databases store data as simple key-value pairs.

##### How They Work:
- **Keys:** Unique identifiers for each piece of data
- **Values:** The actual data, which can be any format
- **High Performance:** Optimized for speed and scale

##### Common Use Cases:
- **Caching:** Storing frequently accessed data
- **Session Storage:** User session information
- **Queue Systems:** Processing background tasks

##### Examples:
- **Redis:** In-memory key-value store
- **Amazon DynamoDB:** Managed NoSQL service

#### 4. Graph Databases

**Relationship-Focused:** These databases excel at storing and querying complex relationships between data points.

##### How They Work:
- **Nodes:** Individual data points
- **Edges:** Relationships between nodes
- **Graph Traversal:** Following connections between related data

##### Common Use Cases:
- **Social Networks:** Friend connections and recommendations
- **Fraud Detection:** Identifying suspicious relationship patterns
- **Knowledge Graphs:** Storing interconnected information

##### Examples:
- **Neo4j:** Leading graph database
- **Amazon Neptune:** Managed graph database service


### Deep Dive: Relational Databases

For our Lightning wallet application, we'll use a relational database. Let's understand why and how they work.

#### The Relational Model

The relational model is based on mathematical set theory and provides a solid foundation for organizing data:

##### Core Concepts:
- **Relations:** Tables that represent entities (users, invoices, payments)
- **Attributes:** Columns that describe properties of entities
- **Tuples:** Rows that represent individual instances
- **Keys:** Special attributes that uniquely identify or connect records

#### Primary and Foreign Keys

Understanding keys is crucial for designing effective databases:

##### Primary Keys:
- **Unique Identifier:** Every table has a primary key that uniquely identifies each row
- **Never Changes:** Primary keys should be stable and never change
- **Usually Integers:** Auto-incrementing integers are common choices
- **Required:** Every table must have a primary key

##### Foreign Keys:
- **References:** Point to primary keys in other tables
- **Relationships:** Create connections between tables
- **Referential Integrity:** Ensure connected data remains consistent
- **Constraints:** Database enforces that foreign keys point to valid records

#### Example: Customers and Orders

Let's look at a classic example:

```sql
-- Customers table
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE
);

-- Orders table
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

In this example:
- Each customer has a unique `id` (primary key)
- Each order references a customer through `customer_id` (foreign key)
- The database ensures every order belongs to a valid customer


### Understanding SQL & Basic Commands

**Structured Query Language (SQL)** is the standard language for working with relational databases. It's been around since the 1970s and is used across virtually all relational database systems.

#### Why SQL Matters

##### Universal Language:
- **Standardized:** Works across different database systems
- **Declarative:** You describe what you want, not how to get it
- **Powerful:** Can handle simple queries to complex analytics
- **Transferable:** Skills apply across many database systems

##### Beyond Developers:
- **Business Analysts:** Query data for insights
- **Data Scientists:** Extract and analyze data
- **Database Administrators:** Manage and optimize databases
- **Many Non-Technical Roles:** Libraries, government, research

#### Basic SQL Commands

The foundation of SQL consists of four main operations:

##### SELECT - Reading Data
```sql
-- Get all users
SELECT * FROM users;

-- Get specific columns
SELECT username, email FROM users;

-- Filter results
SELECT * FROM users WHERE created_at > '2023-01-01';
```

##### INSERT - Adding Data
```sql
-- Add a new user
INSERT INTO users (username, email, password) 
VALUES ('alice', 'alice@example.com', 'hashed_password');
```

##### UPDATE - Modifying Data
```sql
-- Update a user's email
UPDATE users 
SET email = 'newemail@example.com' 
WHERE username = 'alice';
```

##### DELETE - Removing Data
```sql
-- Remove a user
DELETE FROM users WHERE username = 'alice';
```

#### Advanced SQL Features

As you grow more comfortable with SQL, you'll discover powerful features:

- **JOINs:** Combining data from multiple tables
- **Aggregations:** Calculating sums, averages, counts
- **Subqueries:** Nested queries for complex logic
- **Indexes:** Optimizing query performance
- **Transactions:** Ensuring data consistency

### SQL vs NoSQL Trade-offs

Understanding the trade-offs between SQL and NoSQL databases helps you choose the right tool for each project.

#### SQL Databases (Relational)

##### Strengths:
- **ACID Compliance:** Guaranteed data consistency
- **Complex Queries:** Powerful JOIN operations
- **Mature Tools:** Decades of tooling and optimization
- **Standardized:** SQL skills transfer between systems
- **Data Integrity:** Strong constraints prevent bad data

##### Best For:
- **Financial Applications:** Where data consistency is critical
- **Complex Relationships:** When data is highly interconnected
- **Reporting Systems:** Complex analytical queries
- **Traditional Business Applications:** ERP, CRM systems

#### NoSQL Databases (Non-Relational)

##### Strengths:
- **Flexible Schema:** Easy to change data structure
- **Horizontal Scaling:** Can spread across many servers
- **Rapid Development:** Quick to prototype and iterate
- **JSON-Native:** Natural fit for JavaScript applications

##### Best For:
- **Content Management:** Varying document structures
- **Real-time Applications:** High-speed reads and writes
- **Microservices:** Independent, loosely coupled systems
- **Prototyping:** When requirements are still evolving

#### Making the Choice

For our Lightning wallet application, we're choosing SQL because:
- **Data Integrity:** Financial applications need strong consistency
- **Clear Relationships:** Users and invoices have well-defined connections
- **Industry Standard:** SQL skills are valuable in the job market
- **Learning Value:** Understanding SQL provides a solid foundation

## Schema Design
<chapterId>da893e37-0c14-4e50-a9e9-4eea34bd8348</chapterId>

### Understanding Database Schemas

A database schema is like a blueprint for your database. It defines the structure, relationships, and constraints that govern how data is organized and accessed.

#### What is a Schema?

##### Definition:
A schema describes:
- **Tables:** What entities exist in your system
- **Columns:** What attributes each entity has
- **Data Types:** What kind of data each column stores
- **Constraints:** Rules about valid data
- **Relationships:** How tables connect to each other

##### Why Schemas Matter:
- **Data Consistency:** Ensures all data follows the same rules
- **Performance:** Optimized structure improves query speed
- **Documentation:** Serves as a blueprint for developers
- **Validation:** Prevents invalid data from entering the system

#### Schema Design Process

Creating a good schema requires careful planning:

##### 1. Identify Entities
What "things" does your application manage?
- Users
- Invoices
- Payments
- Transactions

##### 2. Define Attributes
What properties does each entity have?
- User: username, password, email, created_at
- Invoice: amount, memo, payment_request, settled

##### 3. Establish Relationships
How do entities connect to each other?
- Users create invoices
- Invoices belong to users
- Payments settle invoices

##### 4. Set Constraints
What rules should the data follow?
- Usernames must be unique
- Amounts must be positive
- Foreign keys must reference valid records

#### Security Considerations

Database security is critical, especially for financial applications:

### Designing Our Pleb Wallet Schema

Let's design the database schema for our Lightning wallet application. We'll use a visual tool to help us plan and understand the relationships.

#### Our Requirements

Based on our application design, we need to store:
- **Users:** People who use our wallet
- **Invoices:** Both invoices we create and invoices we pay
- **Relationships:** Which user owns which invoices

#### Using QuickDB Diagrams

We'll use [QuickDB Diagrams](https://app.quickdatabasediagrams.com/) to visualize our schema. This tool helps us:
- **Visualize Relationships:** See how tables connect
- **Define Constraints:** Specify data rules
- **Generate Code:** Export to actual SQL
- **Collaborate:** Share designs with team members

#### Our Final Schema

Here's our complete database schema for the Pleb Wallet:

```sql
Users
-
id PK int
username string UNIQUE
password string
adminKey string default=null

Invoices
-
id PK int
payment_request string UNIQUE
value int
memo string
fees int
send bool
settled bool
settle_date timestamp
created_at timestamp default=GETUTCDATE()
user_id int FK >- Users.id
```

#### Users Table Breakdown

##### Field Definitions:
- **id:** Primary key, auto-incrementing integer
- **username:** Unique identifier for login
- **password:** Hashed password (never store plain text!)
- **adminKey:** Optional admin key for privileged operations

#### Invoices Table Breakdown

##### Field Definitions:
- **id:** Primary key for the invoice
- **payment_request:** The actual Lightning invoice string (unique)
- **value:** Amount in satoshis
- **memo:** Optional description/message
- **fees:** Routing fees paid (for outgoing payments)
- **send:** Boolean indicating if this is outgoing (true) or incoming (false)
- **settled:** Boolean indicating if the invoice has been paid
- **settle_date:** When the invoice was paid
- **created_at:** When the invoice was created
- **user_id:** Foreign key linking to the user who owns this invoice

#### Understanding the Relationships

The relationship between Users and Invoices is **one-to-many**:
- One user can have many invoices
- Each invoice belongs to exactly one user

This is enforced by the foreign key constraint on `user_id` in the Invoices table.

#### Schema Visualization

When you input this schema into QuickDB, you'll see:
- **Two connected tables** with a line showing the relationship
- **Key icons** indicating primary keys
- **Relationship arrows** showing foreign key connections

### Key Database Concepts

#### Data Types

Understanding data types is crucial for effective schema design:

##### Common Types:
- **INTEGER:** Whole numbers (user IDs, amounts in satoshis)
- **STRING/TEXT:** Text data (usernames, memos)
- **BOOLEAN:** True/false values (settled, send)
- **TIMESTAMP:** Date and time information
- **DECIMAL:** Precise decimal numbers (for fiat amounts)

##### Choosing the Right Type:
- **Storage Efficiency:** Smaller types use less space
- **Query Performance:** Appropriate types enable faster queries
- **Data Integrity:** Types prevent invalid data

#### Constraints

Constraints ensure data quality and consistency:

##### Types of Constraints:
- **PRIMARY KEY:** Unique identifier for each row
- **FOREIGN KEY:** References to other tables
- **UNIQUE:** No duplicate values allowed
- **NOT NULL:** Field must have a value
- **CHECK:** Custom validation rules

##### Example Constraints:
```sql
-- Username must be unique and not null
username string UNIQUE NOT NULL

-- Amount must be positive
value int CHECK (value > 0)

-- Foreign key relationship
user_id int REFERENCES users(id)
```

### Lightning-Specific Considerations

#### Invoice Management

Our schema needs to handle both:
- **Incoming Invoices:** Created by users to receive payments
- **Outgoing Payments:** Invoices we pay to other Lightning nodes

The `send` field helps us distinguish between these two types.

#### Payment States

Lightning payments have several states:
- **Created:** Invoice generated but not yet paid
- **Pending:** Payment in progress
- **Settled:** Payment completed successfully
- **Failed:** Payment attempt failed

Our schema tracks these states using `settled` and `settle_date` fields.

#### Fee Tracking

Lightning payments include routing fees. Our schema tracks:
- **value:** The base amount of the invoice
- **fees:** Additional fees paid for routing
- **Total cost:** value + fees (calculated in application)


#### Password Security

**Never store plain text passwords:**
```javascript
// WRONG - Never do this
const user = {
  username: 'alice',
  password: 'mypassword123'
};

// CORRECT - Always hash passwords
const bcrypt = require('bcrypt');
const hashedPassword = await bcrypt.hash(password, 10);
```

#### Data Validation

**Validate data at multiple levels:**
- **Application Level:** Check data before saving
- **Database Level:** Use constraints and triggers
- **API Level:** Validate incoming requests

#### Access Control

**Principle of least privilege:**
- **Database Users:** Create specific users for your application
- **Permissions:** Grant only necessary permissions
- **Network Security:** Restrict database access by IP/network

### Best Practices and Key Takeaways

#### Naming Conventions

Consistent naming makes your database easier to understand:

##### Table Names:
- **Plural:** `users`, `invoices`, `payments`
- **Lowercase:** Avoid mixed case
- **Descriptive:** Clear about what the table contains

##### Column Names:
- **Lowercase with underscores:** `user_id`, `created_at`
- **Descriptive:** `payment_request` not `pr`
- **Consistent:** Use same patterns throughout

#### Planning for Growth

Design your schema with future growth in mind:

##### Considerations:
- **Scalability:** Will this work with millions of records?
- **Flexibility:** Can we add new features easily?
- **Performance:** Will queries remain fast as data grows?
- **Maintenance:** Is the schema easy to understand and modify?



1. **Databases are Essential:** Every serious backend application needs persistent data storage
2. **Relational Databases are Standard:** SQL databases are the industry standard for most applications
3. **Schema Design Matters:** Good planning upfront saves time and prevents problems later
4. **Relationships are Powerful:** Foreign keys enable complex data relationships
5. **Constraints Ensure Quality:** Use database constraints to prevent invalid data
6. **Security is Critical:** Never store sensitive data in plain text
7. **Planning Prevents Problems:** Design your schema before writing code


#### Practice Exercises and Resources

1. **Explore QuickDB:** Create different schema designs for various applications (blog, e-commerce, social media)
2. **Identify Relationships:** Practice identifying one-to-many, many-to-many, and one-to-one relationships
3. **Design Constraints:** Think about what constraints would be appropriate for different types of data
4. **Research Database Types:** Look into when you might choose MongoDB vs PostgreSQL vs Redis
5. **Study Existing Schemas:** Look at open-source projects to see how they design their databases 

#### Essential Reading
- [Database Design Fundamentals](https://www.lucidchart.com/pages/database-diagram/database-design) - Comprehensive guide to database design
- [SQL Tutorial](https://www.w3schools.com/sql/) - Interactive SQL learning
- [Database Normalization](https://www.studytonight.com/dbms/database-normalization.php) - Understanding normal forms


#### Lightning Development Context
- [Database Design for Bitcoin Apps](https://bitcoin.design/guide/daily-spending-wallet/database-design/) - Specific considerations for Bitcoin applications
- [Lightning Network Database Patterns](https://docs.lightning.engineering/lightning-network-tools/lnd/database) - How Lightning nodes store data

Remember: Database design is both an art and a science. Start with solid fundamentals, but don't be afraid to iterate and improve your designs as you learn more about your application's needs. The schema we've designed for our Lightning wallet is intentionally simple, but it provides a solid foundation that we can build upon as we add more features.

In the next lesson, we'll bring this schema to life by setting up a real database and implementing our design with actual SQL commands! 

## Hands-on SQL Foundations
<chapterId>9a0b7628-bf7b-4c44-ad9c-0f7ec071ed32</chapterId>

**Note:** This lesson provides the SQL foundation you'll need for the next lesson where we'll integrate a real database into our Pleb Wallet backend!

### Basics in SQL

**SQL stands for Structured Query Language.** It's essentially a language that allows us to "communicate" with databases. Let's break down what makes SQL special:

#### Breaking Down the Acronym

**Structured:** SQL is structured, meaning it has a defined format and syntax. The rules and structure of SQL allow us to describe exactly what we want from a database with precision and clarity.

**Query:** A query is a request for data. When you want to retrieve, insert, update, or delete data from a database, you make a query. Think of it as asking questions to your database and getting answers back.

**Language:** SQL is a language designed for a specific purpose - to interact with relational databases. It's been around since the mid-1970s and has become the universal standard for database operations.

#### Why SQL Matters

SQL is probably one of the most widely known programming languages in the world, alongside HTML. Here's why it's so important:

##### Universal Application
Whether your data is stored in:
- A small SQLite database on an IoT device
- A MySQL database powering a web application
- A massive Oracle database running a multinational corporation

SQL provides the means to work with the data consistently across all these environments.

##### Industry Standard
SQL is recognized by the American National Standards Institute (ANSI) and the International Organization for Standardization (ISO). This standardization means:
- Skills transfer between different database systems
- Consistent syntax across platforms
- Long-term career value

##### Core Capabilities
With SQL, you can perform essential database tasks:
- **Retrieving data:** Find specific information that meets your criteria
- **Inserting new data:** Add new records to your tables
- **Updating existing data:** Modify information that's already stored
- **Deleting data:** Remove records that are no longer needed
- **Creating databases and tables:** Build your data structure from scratch
- **Maintaining database structures:** Modify and optimize your database design

### Understanding RDBMS

**RDBMS stands for Relational Database Management System.** This is the foundation that SQL operates on.

#### What Makes a Database "Relational"

The "relational" part refers to how data is organized and connected:

##### Table Structure
- **Tables:** Data is stored in tables, much like spreadsheets
- **Rows:** Each row represents a single record (like one user)
- **Columns:** Each column represents a data field (like username or email)
- **Relationships:** Tables connect to each other through shared keys

##### Mental Model: Multiple Spreadsheets
Imagine you're building a Python program that needs to work with multiple Google Sheets:
- One spreadsheet for customers
- Another spreadsheet for orders
- You need to connect them together with certainty

You'd quickly realize you need:
- Unique identifiers (primary keys)
- Ways to link spreadsheets (foreign keys)
- Rules about data consistency (constraints)

This is exactly what RDBMS provides, but with much more sophistication and reliability.

#### Popular RDBMS Options

The most common relational database management systems include:

##### The Big Three for Developers
- **PostgreSQL:** Advanced features, great for complex applications, popular in production
- **MySQL:** Most popular open-source database, widely supported
- **SQLite:** Lightweight, perfect for development and learning

##### Enterprise Options
- **Oracle:** Enterprise-grade with advanced features
- **SQL Server:** Microsoft's database solution

#### SQL Dialects

While SQL is standardized, each RDBMS has its own "dialect" with slight variations:

##### Common Differences
- **Functions:** Each system has unique built-in functions
- **Data Types:** Slightly different ways to handle data
- **Syntax Extensions:** Proprietary features and optimizations

##### For Beginners
Don't worry about these differences initially. Focus on learning standard SQL - the skills transfer between systems, and you can learn the nuances as needed.

### Fundamental SQL Commands

Let's explore the essential SQL commands you'll use daily. For each command, we'll provide examples and link to additional practice resources.

#### SELECT - Reading Data

**The SELECT command is the most important SQL command.** It's used to retrieve data from your database.

##### Basic Syntax
```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;  -- Select everything
```

##### Examples
```sql
-- Get all users
SELECT * FROM users;

-- Get specific columns
SELECT username, email FROM users;

-- Filter results with WHERE
SELECT * FROM users WHERE created_at > '2023-01-01';
```

##### Key Concepts
- **Result Set:** The data returned is stored in a result table
- **Wildcard (*):** Selects all columns
- **Column Selection:** Choose specific columns for better performance

**Practice Resource:** [W3Schools SELECT Tutorial](https://www.w3schools.com/sql/sql_select.asp)

#### INSERT - Adding Data

**The INSERT INTO statement adds new rows to your tables.**

##### Basic Syntax
```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

##### Examples
```sql
-- Add a new user
INSERT INTO users (username, email, password)
VALUES ('alice', 'alice@example.com', 'hashed_password');

-- Insert multiple rows at once
INSERT INTO users (username, email, password)
VALUES 
  ('bob', 'bob@example.com', 'hashed_password1'),
  ('carol', 'carol@example.com', 'hashed_password2');
```

**Practice Resource:** [W3Schools INSERT Tutorial](https://www.w3schools.com/sql/sql_insert.asp)

#### UPDATE - Modifying Data

**The UPDATE statement modifies existing records in a table.**

##### Basic Syntax
```sql
UPDATE table_name 
SET column1 = value1, column2 = value2
WHERE condition;
```

##### Examples
```sql
-- Update a user's email
UPDATE users 
SET email = 'newemail@example.com' 
WHERE username = 'alice';

-- Update multiple columns
UPDATE users 
SET email = 'alice@newdomain.com', last_login = '2023-12-01'
WHERE id = 1;
```

##### Important Note
Always use a WHERE clause with UPDATE! Without it, you'll update ALL rows in the table.

**Practice Resource:** [W3Schools UPDATE Tutorial](https://www.w3schools.com/sql/sql_update.asp)

#### DELETE - Removing Data

**The DELETE statement removes existing records from a table.**

##### Basic Syntax
```sql
DELETE FROM table_name WHERE condition;
```

##### Examples
```sql
-- Remove a specific user
DELETE FROM users WHERE username = 'alice';

-- Remove users created before a certain date
DELETE FROM users WHERE created_at < '2023-01-01';
```

##### Security Warning
Like UPDATE, always use a WHERE clause! Without it, you'll delete ALL rows.

**Practice Resource:** [W3Schools DELETE Tutorial](https://www.w3schools.com/sql/sql_delete.asp)

#### WHERE - Filtering Data

**The WHERE clause is used to filter records based on specific conditions.**

##### Basic Syntax
```sql
SELECT column1, column2 FROM table_name WHERE condition;
```

##### Examples
```sql
-- Simple equality
SELECT * FROM users WHERE country = 'USA';

-- Numeric comparison
SELECT * FROM invoices WHERE amount > 1000;

-- Multiple conditions
SELECT * FROM users 
WHERE country = 'USA' AND age >= 18;

-- Pattern matching
SELECT * FROM users 
WHERE username LIKE 'admin%';
```

##### Common Operators
- **=** Equal to
- **>** Greater than
- **<** Less than
- **>=** Greater than or equal
- **<=** Less than or equal
- **<>** or **!=** Not equal
- **LIKE** Pattern matching
- **IN** Match any value in a list
- **BETWEEN** Range of values

**Practice Resource:** [W3Schools WHERE Tutorial](https://www.w3schools.com/sql/sql_where.asp)

#### CREATE - Building Structure

**The CREATE command builds databases and tables.**

##### Creating a Database
```sql
CREATE DATABASE my_database;
```

##### Creating a Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

##### Data Types
Common data types you'll use:
- **INTEGER:** Whole numbers
- **TEXT:** String data
- **BOOLEAN:** True/false values
- **TIMESTAMP:** Date and time
- **DECIMAL:** Precise decimal numbers

#### ALTER - Modifying Structure

**The ALTER command modifies existing table structures.**

##### Adding a Column
```sql
ALTER TABLE users 
ADD COLUMN lightning_address TEXT;
```

##### Modifying a Column
```sql
ALTER TABLE users 
MODIFY COLUMN email VARCHAR(255);
```

##### Example Use Case
If you update your Lightning wallet to support Lightning addresses, you might add:
```sql
ALTER TABLE users 
ADD COLUMN lightning_address TEXT DEFAULT NULL;
```

#### DROP - Removing Structure

**The DROP command permanently deletes databases or tables.**

##### Dropping a Table
```sql
DROP TABLE table_name;
```

##### Dropping a Database
```sql
DROP DATABASE database_name;
```

##### ⚠️ Security Warning
The DROP command is permanent! This is the source of the famous "Little Bobby Tables" attack where malicious users try to inject `DROP TABLE` commands through input fields.

**Never allow user input to directly execute DROP commands!**

## Advanced SQL
<chapterId>8226de3b-7b5e-4245-ab69-085054b8cd42</chapterId>

### SQL Joins: Connecting Tables

Joins are where SQL gets sophisticated. They allow you to combine data from multiple tables based on relationships between them.

#### Why Joins Matter

Remember our mental model of multiple spreadsheets? Joins are how you combine those spreadsheets intelligently. You need different strategies depending on what data you want to see.

#### Types of Joins

There are four main types of joins, each serving different purposes:

##### 1. INNER JOIN (Simple Join)
**Returns only records that have matching values in both tables.**

```sql
SELECT customers.customer_name, orders.product
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

**Use Case:** "Show me customers and their orders, but only for customers who have actually placed orders."

##### 2. LEFT JOIN (Left Outer Join)
**Returns all records from the left table, and matched records from the right table.**

```sql
SELECT customers.customer_name, orders.product
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```

**Use Case:** "Show me all customers, including those who haven't placed any orders yet."

##### 3. RIGHT JOIN (Right Outer Join)
**Returns all records from the right table, and matched records from the left table.**

```sql
SELECT customers.customer_name, orders.product
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
```

**Use Case:** "Show me all orders, even if the customer data is missing."

##### 4. FULL OUTER JOIN
**Returns all records when there's a match in either table.**

```sql
SELECT customers.customer_name, orders.product
FROM customers
FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id;
```

**Use Case:** "Show me everything - all customers and all orders, whether they match or not."

#### Practical Example

Let's imagine we have two tables:

**Customers Table:**
| customer_id | customer_name |
|-------------|---------------|
| 1           | John          |
| 2           | Jane          |
| 3           | Alice         |

**Orders Table:**
| order_id | product | customer_id |
|----------|---------|-------------|
| 1        | Apples  | 1           |
| 2        | Bananas | 2           |
| 3        | Grapes  | 2           |
| 4        | Oranges | 4           |

Notice that:
- Alice (customer_id 3) has no orders
- There's an order for customer_id 4, but no customer with that ID

##### INNER JOIN Result
```sql
SELECT customers.customer_name, orders.product
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

| customer_name | product |
|---------------|---------|
| John          | Apples  |
| Jane          | Bananas |
| Jane          | Grapes  |

Only customers with orders appear.

##### LEFT JOIN Result
```sql
SELECT customers.customer_name, orders.product
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```

| customer_name | product |
|---------------|---------|
| John          | Apples  |
| Jane          | Bananas |
| Jane          | Grapes  |
| Alice         | NULL    |

All customers appear, even Alice with no orders.

##### RIGHT JOIN Result
```sql
SELECT customers.customer_name, orders.product
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
```

| customer_name | product |
|---------------|---------|
| John          | Apples  |
| Jane          | Bananas |
| Jane          | Grapes  |
| NULL          | Oranges |

All orders appear, even the orphaned "Oranges" order.

### Building Our Pleb Wallet Database

Now let's apply what we've learned to create the actual database tables for our Lightning wallet application.

#### Our Database Schema

Based on our design from Lesson 8, we need two tables:

##### Users Table
Stores information about wallet users:
- **id:** Primary key
- **username:** Unique identifier for login
- **password:** Hashed password (never plain text!)
- **adminKey:** Optional admin privileges

##### Invoices Table
Stores Lightning invoices (both incoming and outgoing):
- **id:** Primary key
- **payment_request:** The actual Lightning invoice string
- **value:** Amount in satoshis
- **memo:** Optional description
- **fees:** Routing fees paid
- **send:** Boolean (true = outgoing, false = incoming)
- **settled:** Boolean (true = paid, false = unpaid)
- **settle_date:** When the invoice was paid
- **created_at:** When the invoice was created
- **user_id:** Foreign key linking to Users table

#### Creating the Users Table

```sql
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    adminKey TEXT DEFAULT NULL
);
```

##### Breakdown:
- **id INTEGER PRIMARY KEY:** Auto-incrementing unique identifier
- **username TEXT UNIQUE NOT NULL:** Required unique username
- **password TEXT NOT NULL:** Required password field
- **adminKey TEXT DEFAULT NULL:** Optional admin key

#### Creating the Invoices Table

```sql
CREATE TABLE Invoices (
    id INTEGER PRIMARY KEY,
    payment_request TEXT UNIQUE NOT NULL,
    value INTEGER NOT NULL,
    memo TEXT,
    fees INTEGER NOT NULL,
    send BOOLEAN NOT NULL,
    settled BOOLEAN NOT NULL,
    settle_date DATETIME,
    created_at DATETIME DEFAULT (datetime('now')),
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Users(id)
);
```

##### Breakdown:
- **payment_request TEXT UNIQUE NOT NULL:** Lightning invoice string (unique)
- **value INTEGER NOT NULL:** Amount in satoshis
- **memo TEXT:** Optional message (can be NULL)
- **fees INTEGER NOT NULL:** Routing fees (can be 0)
- **send BOOLEAN NOT NULL:** True for outgoing, false for incoming
- **settled BOOLEAN NOT NULL:** Payment status
- **settle_date DATETIME:** When payment completed (NULL if unsettled)
- **created_at DATETIME DEFAULT (datetime('now')):** Auto-timestamp
- **user_id INTEGER NOT NULL:** Foreign key to Users table
- **FOREIGN KEY(user_id) REFERENCES Users(id):** Enforces relationship

#### Understanding the Relationship

The relationship between Users and Invoices is **one-to-many**:
- One user can have many invoices
- Each invoice belongs to exactly one user
- The foreign key constraint ensures data integrity

### Hands-On Practice with SQLite Online

Let's put our knowledge into practice using a browser-based SQL environment.

#### Setting Up SQLite Online

1. Visit [SQLite Online IDE](https://sqliteonline.com/)
2. This tool lets you practice SQL without installing anything
3. You can create, modify, and query databases directly in your browser

#### Practice Exercise: Building Our Schema

Follow these steps to create your Pleb Wallet database:

##### Step 1: Create the Users Table
```sql
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    adminKey TEXT DEFAULT NULL
);
```

##### Step 2: Insert a Test User
```sql
INSERT INTO Users (username, password)
VALUES ('example_user', 'hashed_password_123');
```

##### Step 3: Query the Users Table
```sql
SELECT * FROM Users;
```

##### Step 4: Create the Invoices Table
```sql
CREATE TABLE Invoices (
    id INTEGER PRIMARY KEY,
    payment_request TEXT UNIQUE NOT NULL,
    value INTEGER NOT NULL,
    memo TEXT,
    fees INTEGER NOT NULL,
    send BOOLEAN NOT NULL,
    settled BOOLEAN NOT NULL,
    settle_date DATETIME,
    created_at DATETIME DEFAULT (datetime('now')),
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Users(id)
);
```

##### Step 5: Insert a Test Invoice
```sql
INSERT INTO Invoices (payment_request, value, memo, fees, send, settled, settle_date, user_id)
VALUES ('lnbc1000n1...', 1000, 'Payment for services', 2, 1, 1, '2023-12-01 10:30:00', 1);
```

##### Step 6: Query with a Join
```sql
SELECT Users.username, Invoices.value, Invoices.memo
FROM Users
INNER JOIN Invoices ON Users.id = Invoices.user_id;
```

#### Advanced Practice Exercises

Try these additional exercises to solidify your understanding:

##### Exercise 1: User Management
```sql
-- Create multiple users
INSERT INTO Users (username, password) VALUES 
('alice', 'pass123'),
('bob', 'pass456'),
('charlie', 'pass789');

-- Find all users
SELECT * FROM Users;

-- Update a user's password
UPDATE Users SET password = 'new_password' WHERE username = 'alice';

-- Find users with admin keys
SELECT * FROM Users WHERE adminKey IS NOT NULL;
```

##### Exercise 2: Invoice Queries
```sql
-- Find all settled invoices
SELECT * FROM Invoices WHERE settled = 1;

-- Find invoices over 500 sats
SELECT * FROM Invoices WHERE value > 500;

-- Find outgoing payments
SELECT * FROM Invoices WHERE send = 1;

-- Calculate total fees paid
SELECT SUM(fees) as total_fees FROM Invoices WHERE send = 1;
```

##### Exercise 3: Complex Joins
```sql
-- Show all users and their invoice count
SELECT Users.username, COUNT(Invoices.id) as invoice_count
FROM Users
LEFT JOIN Invoices ON Users.id = Invoices.user_id
GROUP BY Users.id;

-- Show users who have sent payments
SELECT DISTINCT Users.username
FROM Users
INNER JOIN Invoices ON Users.id = Invoices.user_id
WHERE Invoices.send = 1;
```

### Lightning-Specific SQL Considerations

Our Lightning wallet has some unique requirements that affect our SQL design:

#### Payment States
Lightning payments have multiple states:
- **Created:** Invoice generated but not paid
- **Pending:** Payment in progress
- **Settled:** Payment completed
- **Failed:** Payment failed

Our schema tracks these with the `settled` boolean and `settle_date` timestamp.

#### Invoice Types
We handle both:
- **Incoming Invoices:** Created by users to receive payments
- **Outgoing Payments:** Invoices we pay to other Lightning nodes

The `send` boolean distinguishes between these types.

#### Fee Tracking
Lightning payments include routing fees:
- **value:** Base amount of the invoice
- **fees:** Additional routing fees
- **Total cost:** value + fees (calculated in application)

#### Security Considerations

##### Password Security
```sql
-- WRONG - Never store plain text passwords
INSERT INTO Users (username, password) VALUES ('user', 'plaintext123');

-- CORRECT - Always hash passwords in your application
-- The hashed password gets stored, not the plain text
INSERT INTO Users (username, password) VALUES ('user', '$2b$10$...');
```

##### SQL Injection Prevention
Never directly concatenate user input into SQL queries:
```sql
-- DANGEROUS - Don't do this
query = "SELECT * FROM Users WHERE username = '" + userInput + "'";

-- SAFE - Use parameterized queries
query = "SELECT * FROM Users WHERE username = ?";
```
#### Common Pitfalls to Avoid

1. **Forgetting WHERE clauses:** Always double-check UPDATE and DELETE statements
2. **Not using constraints:** PRIMARY KEY, FOREIGN KEY, and UNIQUE constraints prevent data corruption
3. **Ignoring data types:** Choose appropriate data types for better performance and storage
4. **Complex joins too early:** Master simple queries before attempting complex multi-table joins
5. **Security oversights:** Always validate input and use parameterized queries


#### Key Takeaways to start safe

1. **SQL is Universal:** Learning SQL provides a foundation that works across many database systems
2. **Start with Basics:** Master SELECT, INSERT, UPDATE, DELETE, and WHERE before moving to advanced topics
3. **Joins Are Powerful:** Understanding joins lets you work with related data across multiple tables
4. **Practice is Essential:** Use tools like SQLite Online to practice and experiment
5. **Security First:** Never store passwords in plain text, always prevent SQL injection
6. **Schema Design Matters:** Good table design makes queries easier and more efficient
7. **Lightning Context:** Consider the specific needs of Lightning applications in your database design


### Practice Exercises and Resources

1. **SQLite Online Exploration:** 
   - Create different database schemas (blog, e-commerce, social media)
   - Practice all four types of joins with sample data
   - Write queries with multiple WHERE conditions

2. **Lightning Wallet Queries:**
   - Design queries to find all unpaid invoices
   - Calculate total fees paid by each user
   - Find the most recent transactions for each user

3. **Schema Design:**
   - Design a database for a Lightning-powered marketplace
   - Consider what tables and relationships you'd need
   - Write the CREATE TABLE statements

4. **Join Practice:**
   - Create sample data with some mismatched foreign keys
   - Practice each type of join to see the different results
   - Write queries that combine data from multiple tables

5. **Security Research:**
   - Research SQL injection attacks and prevention
   - Learn about database user permissions
   - Study password hashing best practices


#### Essential Learning
- [SQL Cheat Sheet](https://cheatography.com/fetttobse/cheat-sheets/sqlite/) - Visual reference for SQL syntax
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) - Interactive SQL learning with exercises
- [SQLite Online IDE](https://sqliteonline.com/) - Browser-based SQL practice environment

#### Video Resources
- [Learn SQL in 15 Minutes](https://www.youtube.com/watch?v=kbKty5ZVKMY) - Quick SQL fundamentals
- [SQL Joins Explained](https://www.youtube.com/watch?v=9yeOJ0ZMUYw) - Visual explanation of joins
- [Database Design Course](https://www.youtube.com/watch?v=ztHopE5Wnpc) - Complete database design tutorial

#### Articles and References
- [SQL Joins Explained Visually](https://dataschool.com/how-to-teach-people-sql/sql-join-types-explained-visually/) - Great visual guide to joins
- [SQLite vs MySQL vs PostgreSQL](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems) - Database comparison
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection) - Security best practices

#### Lightning Development Context
- [Database Design for Bitcoin Apps](https://bitcoin.design/guide/daily-spending-wallet/database-design/) - Bitcoin-specific database considerations
- [Lightning Network Database Patterns](https://docs.lightning.engineering/lightning-network-tools/lnd/database) - How Lightning nodes store data
- [Bolt 11 Invoice Format](https://github.com/lightning/bolts/blob/master/11-payment-encoding.md) - Understanding Lightning invoice structure

Remember: SQL is both powerful and potentially dangerous. Start with simple queries, always test in a safe environment, and never run queries you don't understand on production data. The fundamentals you learn here will serve you throughout your development career, as SQL skills are transferable across many technologies and industries.

In the next lesson, we'll bring these SQL concepts to life by integrating a real database into our Pleb Wallet backend! 

# Database Dev with Knex.js
<partId>f8de8385-6824-43c1-9438-ffeeea1b3c77</partId>

## Database Development with Knex.js
<chapterId>7f08bc46-d25b-4ff1-810f-cd87833089fa</chapterId>

**Note:** This lesson represents a major milestone in our Lightning wallet backend! We're moving from mock data to real database integration, setting the foundation for our production-ready application.

### The Importance of Knex.js

**Knex.js is like a translator between JavaScript and SQL.** It allows you to write database requests in JavaScript, which is easier for many developers to work with, and then automatically translates these commands into proper SQL.

#### Breaking Down the Benefits

**JavaScript-First Approach:** Instead of writing raw SQL, you can use JavaScript methods and objects to interact with your database. This means:
- Familiar syntax for JavaScript developers
- Better integration with your Node.js application
- Enhanced readability and maintainability

**Database Agnostic:** Knex supports multiple database systems:
- SQLite (perfect for development)
- PostgreSQL (excellent for production)
- MySQL, MariaDB, and others

**Built-in Tools:** Knex comes with powerful features:
- Schema builder for creating tables
- Migration system for version control
- Seeding system for test data
- Query builder for complex operations

#### Knex vs Raw SQL

Here's a comparison to show the difference:

**Raw SQL:**
```sql
CREATE TABLE users (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL
);
```

**Knex.js:**
```javascript
knex.schema.createTable('users', function(table) {
  table.increments('id');
  table.string('name').notNullable();
});
```

The Knex version is more readable and integrates seamlessly with your JavaScript code.

#### Why Use Knex.js?

##### Unified Query Syntax
Knex provides a consistent syntax across different SQL databases. This means you can:
- Write your schema once
- Switch databases with minimal code changes
- Use the same development patterns for local and production environments

##### Schema Builder
Knex's schema builder makes it easy to:
- Create and modify tables
- Define relationships between tables
- Set up constraints and indexes
- Handle complex database structures

##### Migration System
Migrations help you:
- Track database changes over time
- Version control your database structure
- Collaborate with team members effectively
- Roll back changes if needed

##### Seeding Capabilities
Seeds allow you to:
- Populate databases with test data
- Create consistent development environments
- Test your application with known data sets
- Set up reference data

##### Production Features
Knex also provides:
- **Transaction Support:** Ensure data integrity with all-or-nothing operations
- **Connection Pooling:** Manage database connections efficiently
- **Query Optimization:** Built-in performance enhancements

### Setting Up Our Database Configuration

Let's start by installing the necessary packages and setting up our database configuration.

#### Installing Required Packages

First, we need to install three essential packages:

```bash
npm i knex sqlite3 pg
```

**Package Breakdown:**
- **knex:** The main library for database operations
- **sqlite3:** SQLite driver for local development
- **pg:** PostgreSQL driver for production deployment

#### Creating the Knex Configuration File

Knex requires a configuration file called `knexfile.js` in your project root. This file defines settings for different environments.

**Create `knexfile.js`:**

```javascript
module.exports = {
  development: {
    // SQLite configuration for local development
    client: "sqlite3",
    connection: {
      filename: "./db/dev.sqlite3",
    },
    useNullAsDefault: true,
    migrations: {
      directory: "./db/migrations",
    },
    seeds: {
      directory: "./db/seeds",
    },
  },

  production: {
    // PostgreSQL configuration for production
    client: "pg",
    connection: process.env.DATABASE_URL,
    migrations: {
      directory: "./db/migrations",
    },
    seeds: {
      directory: "./db/seeds",
    },
  },
};
```

##### Configuration Breakdown

**Development Environment:**
- **client:** Specifies SQLite3 as the database
- **connection.filename:** Points to our local database file
- **useNullAsDefault:** Ensures compatibility with PostgreSQL patterns
- **migrations.directory:** Where migration files are stored
- **seeds.directory:** Where seed files are stored

**Production Environment:**
- **client:** Specifies PostgreSQL as the database
- **connection:** Uses environment variable for database URL
- **migrations/seeds:** Same directory structure as development

#### Creating the Database Configuration Module

Now we need to create a database configuration module that our application can use.

**Create `db/dbConfig.js`:**

```javascript
const knex = require("knex");
const config = require("../knexfile");

// Determine environment (development or production)
const env = process.env.NODE_ENV || "development";

// Initialize Knex with the appropriate configuration
const db = knex(config[env]);

module.exports = db;
```

This module:
1. Imports the Knex library
2. Imports our configuration
3. Determines the current environment
4. Initializes Knex with the appropriate configuration
5. Exports the database connection for use throughout our application

### Understanding Migrations

**Migrations are like version control for your database structure.** They provide a systematic way to create, modify, and track changes to your database schema over time.

#### What Are Migrations?

Think of migrations as a to-do list for your database. Each migration file contains:
- **Up function:** Instructions for applying changes
- **Down function:** Instructions for reversing changes

#### Why Use Migrations?

1. **Version Control:** Track every change to your database structure
2. **Team Collaboration:** Everyone can see what changes were made and why
3. **Deployment Safety:** Apply changes systematically across environments
4. **Rollback Capability:** Undo changes if something goes wrong

#### How Migrations Work

Each migration file follows this pattern:

```javascript
exports.up = function(knex) {
  // Instructions for making changes
  return knex.schema.createTable('users', function(table) {
    table.increments('id');
    table.string('name');
    table.string('email');
  });
};

exports.down = function(knex) {
  // Instructions for undoing changes
  return knex.schema.dropTable('users');
};
```

#### Creating Our First Migration

Let's create a migration for our Users table:

```bash
npx knex migrate:make create_users_table
```

This command:
- Creates a new migration file with a timestamp prefix
- Generates boilerplate up and down functions
- Stores the file in the migrations directory

#### Users Table Migration

Open the newly created migration file and add this code:

```javascript
exports.up = function (knex) {
  return knex.schema.createTable("users", function (table) {
    // Primary key that auto-increments
    table.increments("id");

    // Username: unique string, max 128 characters, required
    table.string("username", 128).notNullable().unique();

    // Password: string, max 128 characters, required
    table.string("password", 128).notNullable();

    // Admin key: optional string for admin privileges
    table.string("adminKey").defaultTo(null);
  });
};

exports.down = function (knex) {
  return knex.schema.dropTableIfExists("users");
};
```

##### Schema Breakdown

**table.increments("id"):**
- Creates an auto-incrementing primary key
- Automatically indexed for performance

**table.string("username", 128).notNullable().unique():**
- Creates a string column with maximum 128 characters
- Cannot be null (required field)
- Must be unique across all records

**table.string("adminKey").defaultTo(null):**
- Optional field for admin privileges
- Defaults to null if not provided
- Secret field for accessing protected endpoints

#### Running the Migration

Execute the migration with:

```bash
npx knex migrate:latest
```

This command:
- Runs all pending migrations
- Creates the database file if it doesn't exist
- Sets up the table structure according to your schema

### Understanding Seeds

**Seeds are files that populate your database with test data.** They're essential for development and testing because they provide consistent, predictable data to work with.

#### What Are Seeds?

Seeds are JavaScript files that:
- Add initial data to your database tables
- Create consistent development environments
- Provide test data for application testing
- Set up reference data (like user roles or categories)

#### Why Use Seeds?

1. **Consistent Testing:** Always have the same data to test against
2. **Development Efficiency:** Don't manually create test data every time
3. **Team Collaboration:** Everyone works with the same data set
4. **Automated Setup:** Quickly set up new development environments

#### Creating Our First Seed

Create a seed file for users:

```bash
npx knex seed:make 01_users
```

The naming convention `01_users` ensures seeds run in order.

#### Users Seed Implementation

Add this code to your users seed file:

```javascript
const bcrypt = require("bcryptjs");

exports.seed = async function (knex) {
  // Delete all existing entries first
  await knex("users").del();
  
  // Insert test users
  await knex("users").insert([
    {
      id: 1,
      username: "Alice",
      password: bcrypt.hashSync("pass1", 14),
      adminKey: "1234",
    },
    {
      id: 2,
      username: "Bob",
      password: bcrypt.hashSync("pass2", 14),
      adminKey: null,
    },
  ]);
};
```

##### Seed Breakdown

**Password Hashing:**
- Uses bcrypt to hash passwords before storing
- The number `14` is the salt rounds (security parameter)
- Never store plain text passwords in any environment

**Test Users:**
- **Alice:** Admin user with adminKey "1234"
- **Bob:** Regular user without admin privileges

#### Running Seeds

Execute the seed with:

```bash
npx knex seed:run
```

This command:
- Runs all seed files in order
- Clears existing data first
- Inserts fresh test data

## Getting Deep in Knex.Js
<chapterId>86cb9e77-3a60-4ccd-b38b-d6cace223189</chapterId>

### Creating the Invoices Table

Now let's create our second table for Lightning invoices. This table will store both incoming and outgoing Lightning payments.

#### Invoices Migration

Create a new migration:

```bash
npx knex migrate:make create_invoices_table
```

#### Invoices Schema Implementation

Add this comprehensive schema to your invoices migration:

```javascript
exports.up = function (knex) {
  return knex.schema.createTable("invoices", function (table) {
    // Primary key
    table.increments("id").primary();

    // Lightning invoice string (unique identifier)
    table.string("payment_request").notNullable().unique();

    // Amount in satoshis
    table.integer("value").notNullable();

    // Optional memo/description
    table.string("memo");

    // Routing fees (null until paid)
    table.integer("fees");

    // Direction: true = outgoing, false = incoming
    table.boolean("send").notNullable();

    // Payment status: true = paid, false = unpaid
    table.boolean("settled").notNullable();

    // When payment was completed (null if unpaid)
    table.timestamp("settle_date").defaultTo(null);

    // When invoice was created
    table.timestamp("created_at").defaultTo(knex.fn.now());

    // Foreign key to users table
    table.integer("user_id").unsigned().notNullable();
    table.foreign("user_id").references("id").inTable("users");
  });
};

exports.down = function (knex) {
  return knex.schema.dropTableIfExists("invoices");
};
```

##### Schema Breakdown

**Lightning-Specific Fields:**
- **payment_request:** The actual Lightning invoice string
- **value:** Amount in satoshis (Lightning's base unit)
- **memo:** Optional description or note
- **fees:** Routing fees (only known after payment)

**State Tracking:**
- **send:** Distinguishes between incoming and outgoing payments
- **settled:** Tracks whether payment has been completed
- **settle_date:** Timestamp of when payment completed

**Relationships:**
- **user_id:** Foreign key linking to the users table
- **foreign():** Ensures referential integrity

#### Running the Invoices Migration

Execute the migration:

```bash
npx knex migrate:latest
```

#### Creating Invoice Seeds

Create a seed file for invoices:

```bash
npx knex seed:make 02_invoices
```

#### Invoice Seed Implementation

Add test invoice data:

```javascript
exports.seed = async function (knex) {
  // Delete all existing entries
  await knex("invoices").del();
  
  // Insert test invoices
  await knex("invoices").insert([
    {
      // Incoming invoice (not yet paid)
      payment_request: "lnbcrt1u1p...",
      memo: "Test incoming payment",
      value: 1000,
      fees: null,
      send: false,
      settled: false,
      settle_date: null,
      user_id: 1, // Alice's invoice
    },
    {
      // Outgoing payment (completed)
      payment_request: "lnbcrt2u1p...",
      memo: "Test outgoing payment",
      value: 1100,
      fees: 10,
      send: true,
      settled: true,
      settle_date: knex.fn.now(),
      user_id: 2, // Bob's payment
    },
  ]);
};
```

##### Seed Data Explanation

**Incoming Invoice (First Entry):**
- Created by Alice to receive payment
- Not yet paid (settled = false)
- No fees yet (fees = null)
- No settle_date yet

**Outgoing Payment (Second Entry):**
- Payment made by Bob
- Completed (settled = true)
- Includes routing fees (fees = 10)
- Has settlement timestamp

#### Running Invoice Seeds

Execute the seeds:

```bash
npx knex seed:run
```

### Viewing Our Database

Now let's examine our database to verify everything was created correctly.

#### Installing SQLite Browser

For easy database viewing, download SQLite Browser:
- Visit [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)
- Download the appropriate version for your operating system
- Install and launch the application

#### Opening Our Database

1. Launch SQLite Browser
2. Click "Open Database"
3. Navigate to your project's `db/` directory
4. Select `dev.sqlite3`
5. Click "Open"

#### Exploring the Data

**View Users Table:**
1. Click the "Browse Data" tab
2. Select "users" from the table dropdown
3. You should see Alice and Bob with their hashed passwords

**View Invoices Table:**
1. Select "invoices" from the table dropdown
2. You should see both test invoices with all their properties
3. Notice the foreign key relationships (user_id values)

#### Verifying Relationships

You can verify the relationship between users and invoices by noting:
- Alice (user_id: 1) has the incoming invoice
- Bob (user_id: 2) has the outgoing payment
- The foreign key constraint ensures data integrity

### Database Development Workflow

Now that we've completed our initial setup, let's understand the typical workflow for database development with Knex.

#### Development Process

1. **Plan Changes:** Determine what database changes are needed
2. **Create Migration:** Generate a new migration file
3. **Define Schema:** Write the up and down functions
4. **Test Migration:** Run the migration and verify results
5. **Create Seeds:** Add test data for the new structure
6. **Verify Results:** Use SQLite Browser to confirm everything works

#### Best Practices

**Migration Guidelines:**
- Always include both up and down functions
- Test migrations thoroughly before deploying
- Use descriptive migration names
- Keep migrations focused on single changes

**Seed Guidelines:**
- Always clear existing data first
- Use realistic test data
- Include edge cases in your test data
- Keep seeds consistent across team members

**Security Considerations:**
- Never store plain text passwords
- Use proper foreign key constraints
- Validate data types and constraints
- Consider data privacy in seed files

### Lightning Wallet Database Design

Our database design specifically supports Lightning wallet functionality:

#### Payment Flow Support

**Incoming Payments:**
- User creates an invoice (settled = false)
- Invoice gets paid by external party
- We update the invoice (settled = true, settle_date = now)

**Outgoing Payments:**
- User initiates payment (send = true)
- Payment routes through Lightning network
- We record the result (settled = true/false, fees)

#### Data Integrity

**Foreign Key Constraints:**
- Ensures every invoice belongs to a valid user
- Prevents orphaned invoice records
- Maintains referential integrity

**Unique Constraints:**
- Prevents duplicate usernames
- Prevents duplicate payment_request strings
- Ensures data consistency

#### Performance Considerations

**Primary Keys:**
- Auto-incrementing IDs for fast lookups
- Indexed by default for query performance

**Timestamp Tracking:**
- created_at for audit trails
- settle_date for payment history
- Enables time-based queries and reports

#### The Database Development Flowchart

Looking back at our complete setup, here's how all the pieces fit together:

```
┌─────────────────────┐
│   Database          │
│   (SQLite/Postgres) │
└─────────────────────┘
           ↑
           │
┌─────────────────────┐
│   Knex.js           │
│   (Query Builder)   │
└─────────────────────┘
           ↑
    ┌──────┴──────┐
    │             │
┌───────────┐ ┌───────────┐
│ Migrations│ │   Seeds   │
│ (Schema)  │ │ (Test Data)│
└───────────┘ └───────────┘
           ↑
┌─────────────────────┐
│   DB Config         │
│   (Connection)      │
└─────────────────────┘
           ↑
┌─────────────────────┐
│   Application       │
│   (Express Routes)  │
└─────────────────────┘
```

This architecture provides:
- **Separation of Concerns:** Each layer has a specific responsibility
- **Environment Flexibility:** Easy switching between development and production
- **Version Control:** Migrations track all schema changes
- **Testing Support:** Seeds provide consistent test data

### Key Takeaways for what's coming

1. **Knex.js Advantages:** JavaScript-first database development with SQL power
2. **Migration System:** Version control for database structure changes
3. **Seeding Strategy:** Consistent test data for development and testing
4. **Environment Configuration:** Different setups for development and production
5. **Lightning Integration:** Database designed specifically for Lightning wallet functionality
6. **Data Integrity:** Foreign keys and constraints ensure data consistency
7. **Development Workflow:** Systematic approach to database changes

#### Common Pitfalls to Avoid

1. **Missing Down Functions:** Always implement rollback functionality
2. **Forgetting Dependencies:** Run migrations in correct order
3. **Seed Data Conflicts:** Always clear existing data before seeding
4. **Configuration Errors:** Double-check database paths and settings
5. **Security Oversights:** Never store plain text passwords
6. **Schema Mismatches:** Ensure seeds match your schema exactly

#### Practice Exercises and Resources

1. **Schema Design Practice:**
   - Design a migration for a "transactions" table
   - Create relationships between users, invoices, and transactions
   - Write seeds for the new table structure

2. **Migration Scenarios:**
   - Practice creating and rolling back migrations
   - Add new columns to existing tables
   - Modify existing column constraints

3. **Seed Data Creation:**
   - Create realistic Lightning invoice data
   - Build seeds for different user scenarios
   - Test edge cases with seed data

4. **Database Exploration:**
   - Use SQLite Browser to write custom queries
   - Explore relationships between tables
   - Verify data integrity constraints

5. **Environment Setup:**
   - Practice switching between development and production configs
   - Set up a PostgreSQL instance for testing
   - Configure environment variables properly


#### Essential Documentation
- [Knex.js Official Documentation](https://knexjs.org/) - Complete reference guide
- [Knex.js Cheat Sheet](https://devhints.io/knex) - Quick reference for common commands
- [SQLite Browser](https://sqlitebrowser.org/) - Tool for viewing SQLite databases

#### Tutorial Resources
- [Node Backend Walkthrough](https://github.com/AustinKelsay/node-backend-walkthrough) - Complete example implementation
- [Learn Knex.js with PostgreSQL](https://www.youtube.com/watch?v=wfrn21E2NaU) - Video tutorial
- [Knex.js Tutorial for Beginners](https://blog.shahednasser.com/knex-js-tutorial-for-beginners/) - Comprehensive written guide

#### Database Concepts
- [What are Database Migrations](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations) - Understanding migration patterns
- [Database Seeding with Knex](https://dev.to/cesareferrari/database-seeding-with-knex-51gf) - Seeding best practices
- [SQL Relationships and Foreign Keys](https://www.sqlitetutorial.net/sqlite-foreign-key/) - Database relationship concepts

#### Lightning Development Resources
- [Lightning Network Database Patterns](https://docs.lightning.engineering/lightning-network-tools/lnd/database) - How Lightning nodes store data
- [Bitcoin Database Design](https://bitcoin.design/guide/daily-spending-wallet/database-design/) - Bitcoin-specific database considerations
- [Lightning Invoice Format](https://github.com/lightning/bolts/blob/master/11-payment-encoding.md) - Understanding Lightning invoice structure

Remember: Database development is a process, not a single event. Each step builds upon the previous one, and the systematic approach we've learned here will serve you well as your applications grow in complexity. The foundation we've built with Knex.js will make it easy to add new features and maintain your Lightning wallet backend as it evolves.

In our next lesson, we'll bring this database to life by connecting it to our Express server and building the API endpoints that will power our Lightning wallet application! 


## Connecting API and Database
<chapterId>5ecc16dc-96e3-40ad-9fc0-a4943af087c6</chapterId>

**Note:** This lesson represents the culmination of our backend development! By the end, you'll have a fully functional Lightning wallet backend that connects your API to your database seamlessly.

#### The Big Picture: Our Complete Setup

Before we dive into the code, let's understand where we are in our development journey. We've completed all the foundational pieces:

- ✅ **Database Setup:** SQLite with proper schema
- ✅ **Knex Configuration:** Migrations and seeds running
- ✅ **API Endpoints:** Express routes with middleware
- ✅ **Lightning Integration:** LND connection established
- ✅ **Authentication:** JWT-based user auth

Now we need to connect these systems together with **database models** - the bridge between our API and our database.

### What Are Database Models in Knex.js?

**Database models are the defined structures and helper functions that provide an interface for querying and manipulating data stored in your database tables.**

Think of models as translators between your JavaScript code and your SQL database. They provide a clean, consistent way to:

#### Core Responsibilities

**Data Representation:**
- Each model typically represents one table in your database
- A `User` model represents the `users` table
- An `Invoice` model represents the `invoices` table

**Query Interface:**
- Models provide methods for common database operations
- `findAll()` - retrieve all records
- `findByUsername()` - find specific records
- `create()` - insert new records
- `update()` - modify existing records
- `delete()` - remove records

**Abstraction Layer:**
- Hide complex SQL queries behind simple JavaScript methods
- Provide consistent error handling
- Enable code reuse across different endpoints

#### Why Use Models?

**Separation of Concerns:**
```javascript
// Without models (bad):
router.get('/users', (req, res) => {
  db('users').select('*').then(users => {
    // Database logic mixed with route logic
  });
});

// With models (good):
router.get('/users', (req, res) => {
  User.findAll().then(users => {
    // Clean separation of concerns
  });
});
```

**Reusability:**
Models can be used across multiple endpoints, reducing code duplication.

**Maintainability:**
Changes to database structure only require updates in one place.

### Setting Up the Database Models Directory

Let's start by organizing our code properly:

#### Creating the Models Directory

```bash
mkdir db/models
```

Your `db` folder should now look like this:
```
db/
├── dbConfig.js
├── dev.sqlite3
├── migrations/
├── seeds/
└── models/        # <- New directory
```

#### Understanding dbConfig.js

Before we create models, let's remember what `dbConfig.js` does:

```javascript
const knex = require("knex");
const config = require("../knexfile");

// Determine environment (development or production)
const env = process.env.NODE_ENV || "development";

// Initialize Knex with the appropriate configuration
const db = knex(config[env]);

module.exports = db;
```

This file:
1. Imports the Knex library
2. Loads our configuration from `knexfile.js`
3. Determines the current environment
4. Creates a database connection
5. Exports the connection for use in models

### Creating the User Model

Let's create our first model for user operations.

#### Create `db/models/user.js`

```javascript
// First, we require our configured instance of knex from the dbConfig.js file.
const db = require("../dbConfig");

// We export an object with several methods, each representing a different database operation
module.exports = {
  // The findAll method retrieves all records from the 'users' table
  findAll: () => {
    return db("users");
  },
  
  // The findByUsername method retrieves the first record where username matches
  findByUsername: (username) => {
    return db("users").where({ username }).first();
  },
  
  // The create method inserts a new record into the 'users' table
  create: (user) => {
    return db("users").insert(user).returning("*");
  },
  
  // The update method finds a user by id and updates their record
  update: (id, user) => {
    return db("users").where({ id }).update(user).returning("*");
  },
  
  // The delete method removes a user record by id
  delete: (id) => {
    return db("users").where({ id }).del();
  },
};
```

#### Breaking Down the User Model

**Method Patterns:**
Each method returns a Knex query, which returns a Promise. This allows us to use `.then()` and `.catch()` in our endpoints.

**findAll():**
- Simple query to get all users
- Returns: `Promise<User[]>`

**findByUsername(username):**
- Uses `.where()` to filter by username
- Uses `.first()` to get only one result
- Returns: `Promise<User | undefined>`

**create(user):**
- Uses `.insert()` to add a new record
- Uses `.returning("*")` to get the created user back
- Returns: `Promise<User>`

**update(id, user):**
- Uses `.where({ id })` to find the specific user
- Uses `.update(user)` to apply changes
- Returns: `Promise<User>`

**delete(id):**
- Uses `.where({ id })` to find the user
- Uses `.del()` to remove the record
- Returns: `Promise<number>` (number of deleted rows)

### Updating User Endpoints (Auth Logic)

Now let's update our user endpoints to use the database models.

#### Adding Required Imports

First, update `routers/usersRouter.js` with the necessary imports:

```javascript
const User = require("../db/models/user");
const authenticate = require("./middleware/authenticate.js");
const authenticateAdmin = require("./middleware/authenticateAdmin.js");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
```

#### Updating GET All Users Endpoint

Replace the existing GET `/` endpoint:

```javascript
// GET all users
// Before processing the request, we apply the 'authenticateAdmin' middleware
router.get("/", authenticateAdmin, (req, res) => {
  // Call the 'findAll' method from our User model
  User.findAll()
    .then((users) => {
      // If successful, send back status 200 with the users
      res.status(200).json(users);
    })
    .catch((err) => {
      // If error occurs, send back status 500 with the error
      res.status(500).json(err);
    });
});
```

**Key Changes:**
- Added `authenticateAdmin` middleware (only admins can see all users)
- Replaced mock data with `User.findAll()`
- Added proper error handling with `.catch()`

#### Updating GET User by Username Endpoint

Replace the existing GET `/user` endpoint:

```javascript
// GET user by their username
// Using 'authenticate' middleware to verify the client's JWT token
router.get("/user", authenticate, async (req, res) => {
  // Get the JWT from the 'authorization' header
  const token = req.headers.authorization;
  // Retrieve the secret key for JWT verification from environment variables
  const secret = process.env.JWT_SECRET;

  // Use the 'verify' method to decode the token
  jwt.verify(token, secret, (err, decodedToken) => {
    // If error occurred during token decoding, respond with 401
    if (err) {
      res.status(401).json({ message: "Error decoding token", Error: err });
    }
    
    // If token was successfully decoded, find user by username
    User.findByUsername(decodedToken.username)
      .then((user) => {
        // If user found, respond with status 200 and user data
        res.status(200).json(user);
      })
      .catch((err) => {
        // If error occurred, respond with status 500 and error
        res.status(500).json(err);
      });
  });
});
```

**Key Changes:**
- Extract username from JWT token
- Use `User.findByUsername()` to get user from database
- Handle both JWT errors and database errors

#### Updating Register Endpoint

Replace the existing POST `/register` endpoint:

```javascript
// POST a user to register
router.post("/register", (req, res) => {
  // Use bcrypt to hash the password before storing in database
  // The '14' is the cost factor for hashing complexity
  const hash = bcrypt.hashSync(req.body.password, 14);

  // Replace the plain text password with the hashed version
  req.body.password = hash;

  // Create new user record in database
  User.create(req.body)
    .then((user) => {
      // If successful, respond with status 201 (Created) and user data
      res.status(201).json({ data: user });
    })
    .catch((err) => {
      // If error occurs, respond with status 500 and error
      res.status(500).json({ error: err });
    });
});
```

**Key Changes:**
- Hash password with bcrypt before saving
- Use `User.create()` to insert into database
- Changed status code to 201 (Created) for proper REST semantics

#### Updating Login Endpoint

Replace the existing POST `/login` endpoint:

```javascript
// POST a user to login
router.post("/login", (req, res) => {
  // Extract username and password from request body
  const { username, password } = req.body;

  // Find user by username in database
  User.findByUsername(username)
    .then((user) => {
      // Check if user exists and password matches
      if (user && bcrypt.compareSync(password, user.password)) {
        // If valid, generate JWT token
        const token = generateToken(user);
        // Respond with success message, token, and user data
        res.status(200).json({ 
          message: `Welcome ${user.username}!`, 
          token, 
          user 
        });
      } else {
        // If invalid credentials, respond with 401
        res.status(401).json({ message: "Invalid credentials" });
      }
    })
    .catch((err) => {
      // If database error, respond with 500
      res.status(500).json({ error: err });
    });
});
```

**Key Changes:**
- Removed mock user data
- Use `User.findByUsername()` to get real user from database
- Compare provided password with stored hash using bcrypt
- Generate JWT token with actual user data

#### Updating Update User Endpoint

Replace the existing PUT `/:id` endpoint:

```javascript
// PUT a user to update them
// Using 'authenticateAdmin' middleware for admin-only access
router.put("/:id", authenticateAdmin, (req, res) => {
  // Call the 'update' method with user ID and request body
  User.update(req.params.id, req.body)
    .then((user) => {
      // If successful, respond with status 200 and updated user
      res.status(200).json(user);
    })
    .catch((err) => {
      // If error occurs, respond with status 500 and error
      res.status(500).json(err);
    });
});
```

**Key Changes:**
- Use `req.params.id` to get user ID from URL
- Use `User.update()` to modify database record
- Only update fields provided in request body

#### Updating Delete User Endpoint

Replace the existing DELETE `/:id` endpoint:

```javascript
// DELETE a user
router.delete("/:id", authenticateAdmin, (req, res) => {
  // Call the 'delete' method with user ID from URL parameters
  User.delete(req.params.id)
    .then((result) => {
      // If successful, respond with status 200 and success message
      res.status(200).json({ message: "User deleted successfully" });
    })
    .catch((err) => {
      // If error occurs, respond with status 500 and error
      res.status(500).json(err);
    });
});
```

**Key Changes:**
- Use `User.delete()` to remove user from database
- Return success message instead of user data

#### Updating Authentication Middleware

Our middleware also needs to be updated to use the database instead of mock data.

#### Update `routers/middleware/authenticateAdmin.js`

```javascript
const jwt = require("jsonwebtoken");
const User = require("../../db/models/user");

module.exports = (req, res, next) => {
  // Extract token from request header
  const token = req.headers.authorization;
  
  // Get JWT secret and admin key from environment variables
  const secret = process.env.JWT_SECRET || "Satoshi Nakamoto";
  const key = process.env.ADMIN_KEY || "1234";

  // If token is present, verify it
  if (token) {
    jwt.verify(token, secret, async (err, decodedToken) => {
      // If token verification fails, return 401
      if (err || !decodedToken) {
        res.status(401).json({ message: "Error with your verification" });
      } else {
        // If token is valid, find user in database
        const user = await User.findByUsername(decodedToken.username);
        
        // Extract admin key from user object
        const adminKey = user?.adminKey?.toString() ?? "";
        
        // Check if user's admin key matches environment admin key
        if (adminKey !== key) {
          // If admin key doesn't match, return 401
          res.status(401).json({ message: "Must be an admin" });
        } else {
          // If admin key matches, continue to next middleware/endpoint
          next();
        }
      }
    });
  } else {
    // If no token present, return 401
    res.status(401).json({ message: "No token!" });
  }
};
```

**Key Changes:**
- Removed mock user data
- Use `User.findByUsername()` to get real user from database
- Check actual admin key from user record
- Added proper error handling for database operations

Let's test our updated user endpoints to ensure everything works correctly.

#### Testing Flow with Postman

We'll go through a complete user lifecycle to test all endpoints:

1. **Register a new user** with admin privileges
2. **Login** to get a JWT token
3. **Get user by username** using the token
4. **Update the user** (requires re-login after username change)
5. **Get all users** (admin endpoint)
6. **Delete the user** (admin endpoint)

#### Step 1: Register a New User

**POST** `http://localhost:3000/api/users/register`

```json
{
  "username": "testuser",
  "password": "testpass",
  "adminKey": "1234"
}
```

**Expected Response:**
```json
{
  "data": {
    "id": 3,
    "username": "testuser",
    "password": "$2a$14$...",
    "adminKey": "1234"
  }
}
```

#### Step 2: Login

**POST** `http://localhost:3000/api/users/login`

```json
{
  "username": "testuser",
  "password": "testpass"
}
```

**Expected Response:**
```json
{
  "message": "Welcome testuser!",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 3,
    "username": "testuser",
    "password": "$2a$14$...",
    "adminKey": "1234"
  }
}
```

Copy the token for subsequent requests.

#### Step 3: Get User by Username

**GET** `http://localhost:3000/api/users/user`

**Headers:**
```
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Expected Response:**
```json
{
  "id": 3,
  "username": "testuser",
  "password": "$2a$14$...",
  "adminKey": "1234"
}
```

#### Step 4: Update User

**PUT** `http://localhost:3000/api/users/3`

**Headers:**
```
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Body:**
```json
{
  "username": "updateduser"
}
```

**Expected Response:**
```json
{
  "id": 3,
  "username": "updateduser",
  "password": "$2a$14$...",
  "adminKey": "1234"
}
```

#### Step 5: Login Again (Username Changed)

Since we updated the username, we need a new token:

**POST** `http://localhost:3000/api/users/login`

```json
{
  "username": "updateduser",
  "password": "testpass"
}
```

#### Step 6: Get All Users (Admin Endpoint)

**GET** `http://localhost:3000/api/users/`

**Headers:**
```
Authorization: [new-token-from-step-5]
```

**Expected Response:**
```json
[
  {
    "id": 1,
    "username": "Alice",
    "password": "$2a$14$...",
    "adminKey": "1234"
  },
  {
    "id": 2,
    "username": "Bob",
    "password": "$2a$14$...",
    "adminKey": null
  },
  {
    "id": 3,
    "username": "updateduser",
    "password": "$2a$14$...",
    "adminKey": "1234"
  }
]
```

#### Step 7: Delete User

**DELETE** `http://localhost:3000/api/users/3`

**Headers:**
```
Authorization: [admin-token]
```

**Expected Response:**
```json
{
  "message": "User deleted successfully"
}
```

## Persisting Lightning Data
<chapterId>191d4c63-e18c-44c8-91bb-b9276c736da7</chapterId>

### Creating the Invoice Model

Now let's create the model for our Lightning invoice operations.

#### Create `db/models/invoice.js`

```javascript
// First, we require our configured instance of knex from the dbConfig.js file.
const db = require("../dbConfig");

module.exports = {
  // The findAll method retrieves all records from the 'invoices' table
  findAll: () => {
    return db("invoices");
  },
  
  // The findOne method retrieves an invoice by payment_request
  findOne: (payment_request) => {
    return db("invoices").where({ payment_request }).first();
  },
  
  // The create method inserts a new invoice record
  create: (invoice) => {
    return db("invoices").insert(invoice).returning("*");
  },
  
  // The update method finds an invoice by payment_request and updates it
  update: (payment_request, invoice) => {
    return db("invoices")
      .where({ payment_request })
      .update(invoice)
      .returning("*");
  },
  
  // The delete method removes an invoice by id
  delete: (id) => {
    return db("invoices").where({ id }).del();
  },
};
```

#### Invoice Model Specifics

**Why use `payment_request` instead of `id`?**
- Payment requests are unique identifiers in Lightning
- They're used to identify invoices across different systems
- More natural for Lightning operations than database IDs

**findOne(payment_request):**
- Lightning-specific lookup method
- Used to check if an invoice exists before updating
- Critical for the invoice event stream

### Updating Invoice Endpoints

Let's update our Lightning router to use the invoice model.

#### Adding Invoice Import

Add to `routers/lightningRouter.js`:

```javascript
const Invoice = require("../db/models/invoice");
```

#### Updating GET All Invoices Endpoint

Replace the existing GET `/invoices` endpoint:

```javascript
// GET all invoices from the database
router.get("/invoices", (req, res) => {
  // Call the 'findAll' method from our Invoice model
  Invoice.findAll()
    .then((invoices) => {
      // If successful, send back status 200 with invoices
      res.status(200).json(invoices);
    })
    .catch((err) => {
      // If error occurs, send back status 500 with error
      res.status(500).json(err);
    });
});
```

**Key Changes:**
- No authentication required (transaction history is public in our app)
- Use `Invoice.findAll()` to get all invoices from database
- Return all invoice data including payment status

#### Updating Create Invoice Endpoint

Replace the existing POST `/invoice` endpoint:

```javascript
// POST required info to create an invoice
router.post("/invoice", authenticate, (req, res) => {
  // Extract value, memo, and user_id from request body
  const { value, memo, user_id } = req.body;
  
  // Call the createInvoice function with the extracted data
  createInvoice({ value, memo, user_id })
    .then((invoice) => {
      // If successful, respond with status 200 and invoice data
      res.status(200).json(invoice);
    })
    .catch((err) => {
      // If error occurs, respond with status 500 and error
      res.status(500).json(err);
    });
});
```

**Key Changes:**
- Extract `user_id` from request body
- Pass all required data to `createInvoice` function
- The function will handle both LND and database operations

### Updating Lightning Functions

Our Lightning functions in `lnd.js` need to be updated to work with the database.

#### Updating createInvoice Function

Replace the existing `createInvoice` function in `lnd.js`:

```javascript
const createInvoice = async ({ value, memo, user_id }) => {
  // Use LND's addInvoice method to create a Lightning invoice
  const invoice = await lnd.services.Lightning.addInvoice({
    value: value,
    memo: memo,
  });

  // After creating the Lightning invoice, save it to our database
  await Invoice.create({
    payment_request: invoice.payment_request,
    value: value,
    memo: memo,
    settled: false,  // New invoice starts as unpaid
    send: false,     // This is an incoming invoice
    user_id: user_id,
  });

  // Return the Lightning invoice data
  return invoice;
};
```

**Key Changes:**
- Added database import: `const Invoice = require("./db/models/invoice");`
- Save invoice to database immediately after creating with LND
- Set appropriate initial values for database fields
- Link invoice to specific user with `user_id`

#### Updating Invoice Event Stream

The invoice event stream listens for payment notifications from LND and updates our database accordingly.

Replace the existing `invoiceEventStream` function:

```javascript
const invoiceEventStream = async () => {
  await lnd.services.Lightning.subscribeInvoices({
    add_index: 0,
    settle_index: 0,
  })
    .on("data", async (data) => {
      // Only process settled (paid) invoices
      if (data.settled) {
        // Check if the invoice exists in our database
        const existingInvoice = await Invoice.findOne(data.payment_request);

        // If invoice exists, update it to reflect payment
        if (existingInvoice) {
          await Invoice.update(data.payment_request, {
            settled: data.settled,           // Mark as paid
            settle_date: data.settle_date,   // Record payment timestamp
          });
          console.log("Invoice updated in database:", data.payment_request);
        } else {
          console.log("Invoice not found in database:", data.payment_request);
        }
      }
    })
    .on("error", (err) => {
      console.log("Invoice event stream error:", err);
    });
};
```

**Key Changes:**
- Use `Invoice.findOne()` to check if invoice exists
- Use `Invoice.update()` to mark invoice as paid
- Handle case where invoice doesn't exist in database
- Added logging for debugging

#### Updating Pay Invoice Endpoint

Replace the existing POST `/pay` endpoint:

```javascript
router.post("/pay", authenticateAdmin, async (req, res) => {
  // Extract payment_request and user_id from request body
  const { payment_request, user_id } = req.body;

  // Attempt to pay the invoice using LND
  const pay = await payInvoice({ payment_request });

  // If payment error occurred, return error
  if (pay.payment_error) {
    res.status(500).json(pay.payment_error);
  }

  // If payment was successful, save to database
  if (pay?.payment_route) {
    const payment = await Invoice.create({
      payment_request: payment_request,
      send: true,                                    // This is an outgoing payment
      value: pay.payment_route.total_amt,           // Total amount paid
      fees: pay.payment_route.total_fees,           // Routing fees
      settled: true,                                // Payment completed instantly
      settle_date: Date.now(),                      // Payment timestamp
      user_id: user_id                              // User who made the payment
    });

    // Return the payment record
    res.status(200).json(payment);
  }
});
```

**Key Changes:**
- Added `user_id` parameter to track who made the payment
- Save outgoing payment to database immediately
- Record all payment details including fees
- Set `send: true` to indicate outgoing payment

### Testing Invoice Endpoints and Debugging

Let's test our updated invoice endpoints with both Postman and Polar.

#### Prerequisites

1. **Start your server**: `npm run start`
2. **Start Polar**: Open Docker Desktop, then open Polar
3. **Start your network**: Click on your network and start it
4. **Verify connection**: Check that your `.env` file has correct LND credentials

#### Testing Flow

1. **Login as Alice** to get admin token
2. **Create an invoice** through the API
3. **Check database** to see the unpaid invoice
4. **Pay the invoice** from Bob's node in Polar
5. **Check database** to see the invoice marked as paid
6. **Create an invoice** from Bob in Polar
7. **Pay the invoice** through our API
8. **Verify the payment** in the database

#### Step 1: Login as Alice

**POST** `http://localhost:3000/api/users/login`

```json
{
  "username": "Alice",
  "password": "pass1"
}
```

Copy the token for subsequent requests.

#### Step 2: Create Invoice Through API

**POST** `http://localhost:3000/api/invoices/invoice`

**Headers:**
```
Authorization: [alice-token]
```

**Body:**
```json
{
  "value": 100,
  "memo": "Test invoice from API",
  "user_id": 1
}
```

**Expected Response:**
```json
{
  "payment_request": "lnbcrt1u1p...",
  "r_hash": "...",
  "add_index": "1"
}
```

#### Step 3: Check All Invoices

**GET** `http://localhost:3000/api/invoices/invoices`

You should see your new invoice with `settled: false`.

#### Step 4: Pay Invoice from Bob

1. In Polar, click on Bob's node
2. Click "Pay Invoice"
3. Paste the payment request from Step 2
4. Click "Pay Invoice"

#### Step 5: Check Invoice Status

**GET** `http://localhost:3000/api/invoices/invoices`

You should now see the invoice with `settled: true` and a `settle_date`.

#### Step 6: Create Invoice from Bob

1. In Polar, click on Bob's node
2. Click "Create Invoice"
3. Set amount to 1000 sats
4. Set memo to "Test payment to Bob"
5. Click "Create Invoice"
6. Copy the payment request

#### Step 7: Pay Invoice Through API

**POST** `http://localhost:3000/api/invoices/pay`

**Headers:**
```
Authorization: [alice-token]
```

**Body:**
```json
{
  "payment_request": "[bob-payment-request]",
  "user_id": 1
}
```

**Expected Response:**
```json
{
  "payment_request": "lnbcrt10u1p...",
  "send": true,
  "value": 1000,
  "fees": 0,
  "settled": true,
  "settle_date": "2024-01-01T12:00:00.000Z",
  "user_id": 1
}
```

#### Step 8: Verify Final State

**GET** `http://localhost:3000/api/invoices/invoices`

You should see both invoices:
- One incoming (paid by Bob): `send: false`, `settled: true`
- One outgoing (paid to Bob): `send: true`, `settled: true`

#### Common Issues and Debugging

#### SQLite Constraint Errors

**Error:** `SQLite constraint: NOT NULL constraint failed: invoices.user_id`

**Solution:** Ensure all required fields are provided in your request body:
```json
{
  "payment_request": "lnbc...",
  "user_id": 1  // Don't forget this!
}
```

#### Token Errors

**Error:** `Must be an admin`

**Solution:** 
1. Verify your admin key in `.env` matches the user's `adminKey`
2. Check that you're using the correct token
3. Ensure the token hasn't expired

#### Database Connection Issues

**Error:** `Database is locked`

**Solution:**
1. Make sure only one instance of your server is running
2. Close any SQLite browser connections
3. Restart your server

#### LND Connection Issues

**Error:** `No connection to LND`

**Solution:**
1. Verify Polar is running
2. Check your `.env` file has correct paths
3. Ensure the LND node is started in Polar

#### The Complete Data Flow

Understanding how data flows through our system:

```
1. User Request → Express Route → Middleware → Controller
2. Controller → Model → Database Query → Results
3. Results → Controller → Response → User

Lightning Flow:
1. Create Invoice → LND → Database → Response
2. Invoice Paid → LND Event → Database Update
3. Pay Invoice → LND → Database → Response
```

#### Example: Creating an Invoice

1. **POST** `/invoice` with `{ value: 100, memo: "test", user_id: 1 }`
2. **Middleware** validates JWT token
3. **Controller** calls `createInvoice()` function
4. **createInvoice()** calls LND to create Lightning invoice
5. **createInvoice()** calls `Invoice.create()` to save to database
6. **Database** stores invoice with `settled: false`
7. **Response** returns Lightning invoice data
8. **Event Stream** listens for payment
9. **Payment Occurs** → Event Stream updates database
10. **Database** now shows `settled: true`

### Practice Exercises and Resources

1. **Add New Model Methods:**
   - Create a `findByUserId()` method in the Invoice model
   - Add a `findByDateRange()` method for invoice history

2. **Enhanced Error Handling:**
   - Add custom error messages for different failure scenarios
   - Implement retry logic for failed database operations

3. **Database Optimization:**
   - Add indexes to frequently queried fields
   - Create compound queries for complex operations

4. **Security Enhancements:**
   - Add input validation to all model methods
   - Implement rate limiting for API endpoints

5. **Lightning Features:**
   - Add support for invoice expiration
   - Implement webhook notifications for payments


#### Essential Documentation
- [Knex.js Query Builder](https://knexjs.org/guide/query-builder.html) - Complete query reference
- [Express.js Error Handling](https://expressjs.com/en/guide/error-handling.html) - Proper error handling patterns
- [JWT Best Practices](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/) - Security considerations

#### Debugging Tools
- [SQLite Browser](https://sqlitebrowser.org/) - View database contents
- [Postman](https://www.postman.com/) - API testing
- [Polar](https://lightningpolar.com/) - Lightning network testing

#### Lightning Development
- [LND API Documentation](https://lightning.engineering/api-docs/) - Complete LND reference
- [Lightning Network Specifications](https://github.com/lightning/bolts) - Protocol details

Remember: Database integration is where your application becomes truly functional. Take time to understand each piece and test thoroughly. The systematic approach we've learned here will serve you well as your Lightning applications grow in complexity!

The next lesson will bring everything together by connecting our backend to a frontend application, creating a complete full-stack Lightning wallet experience.

# Setup the Full-Stack Application seccion
<partId>4e8b0dbf-81c8-4f40-a087-6a3adb9bee9e</partId>


## Full-Stack Frontend Architecture
<chapterId>d221e6bd-37ff-459c-993c-3a22a65df0a0</chapterId>

### Understanding the Pleb Wallet Frontend

Before we dive into the frontend integration, let's appreciate what we've accomplished:

- ✅ **Backend Server:** Express.js API with proper routing
- ✅ **Database System:** SQLite with Knex.js migrations and seeds
- ✅ **Lightning Integration:** LND connection with invoice/payment functionality
- ✅ **User Authentication:** JWT-based auth with admin permissions
- ✅ **Database Models:** Clean abstraction layer for data operations
- ✅ **Complete API:** All endpoints tested and working with Postman/Insomnia

Now we're ready to provide a user-friendly interface that makes all this functionality accessible to real users!

The Pleb Wallet is a React-based Lightning wallet interface that provides:

#### Core Features

**Lightning Operations:**
- Create Lightning invoices for receiving payments
- Pay Lightning invoices for sending payments
- Real-time balance updates
- Transaction history display

**User Management:**
- User registration and login
- JWT token-based authentication
- Role-based permissions (admin vs regular users)

**Visual Interface:**
- Bitcoin price chart with real-time updates
- Transaction list with payment details
- Modal-based invoice creation and payment flows
- Clean, responsive design

#### Frontend Architecture

The Pleb Wallet follows a simple but effective React architecture:

```
src/
├── App.js              # Main application component
├── components/
│   ├── Header.js       # Navigation and user info
│   ├── Buttons.js      # Send/Receive action buttons
│   ├── Chart.js        # Bitcoin price chart
│   ├── Transactions.js # Transaction history display
│   └── PaymentsModal.js # Invoice creation/payment modal
└── utils/
    └── axiosWithAuth.js # HTTP client with JWT auth
```

**Key Concepts:**
- **Single Page Application (SPA):** All functionality in one page
- **Component-Based:** Modular React components for different features
- **State Management:** React hooks for managing application state
- **API Integration:** Axios for HTTP requests to our backend
- **Real-time Updates:** Periodic polling for fresh data

#### Getting the Updated Frontend

##### Option 1: Clone the Updated Repository

The easiest way to get started is to clone the pre-updated frontend:

```bash
git clone https://github.com/plebdevs/pleb-wallet-frontend.git
cd pleb-wallet-frontend
npm install
```

##### Option 2: Update Your Existing Frontend

If you have the original frontend from Course #1, you can update it manually by following the changes we'll outline in this lesson.

### Frontend Architecture Walkthrough

Let's examine the key components and understand how they work with our backend.

#### App.js - The Main Application

The heart of our application contains all the core logic:

```javascript
import React, { useState, useEffect } from 'react';
import axiosWithAuth from './utils/axiosWithAuth';
import Header from './components/Header';
import Buttons from './components/Buttons';
import Chart from './components/Chart';
import Transactions from './components/Transactions';
import PaymentsModal from './components/PaymentsModal';

const App = () => {
  // State for various data
  const [price, setPrice] = useState(0);
  const [walletBalance, setWalletBalance] = useState(0);
  const [channelBalance, setChannelBalance] = useState(0);
  const [transactions, setTransactions] = useState([]);
  const [chartData, setChartData] = useState([]);
  const [user, setUser] = useState(null);
  const [modalState, setModalState] = useState('');

  // Backend URL from environment variables
  const backendUrl = process.env.REACT_APP_BACKEND_URL;

  // Authentication token handling
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // Get user info when token exists
      getUserInfo();
    }
  }, []);

  // Function to get Bitcoin price from Coinbase API
  const getPrice = () => {
    fetch("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
      .then(res => res.json())
      .then(data => {
        setPrice(data.data.rates.USD);
      });
  };

  // Function to get wallet balance from our backend
  const getWalletBalance = () => {
    axiosWithAuth()
      .get(`${backendUrl}/lightning/balance`)
      .then(res => {
        setWalletBalance(res.data.total_balance);
      })
      .catch(err => console.log(err));
  };

  // Function to get channel balance from our backend
  const getChannelBalance = () => {
    axiosWithAuth()
      .get(`${backendUrl}/lightning/channelbalance`)
      .then(res => {
        setChannelBalance(res.data.balance);
      })
      .catch(err => console.log(err));
  };

  // Function to get transactions from our backend
  const getTransactions = () => {
    axiosWithAuth()
      .get(`${backendUrl}/lightning/invoices`)
      .then(res => {
        setTransactions(res.data);
      })
      .catch(err => console.log(err));
  };

  // Function to get user info
  const getUserInfo = () => {
    axiosWithAuth()
      .get(`${backendUrl}/users/user`)
      .then(res => {
        setUser(res.data);
      })
      .catch(err => console.log(err));
  };

  // Initial data loading
  useEffect(() => {
    getPrice();
    getWalletBalance();
    getChannelBalance();
    getTransactions();
  }, []);

  // Periodic updates
  useEffect(() => {
    const interval = setInterval(() => {
      getPrice();
      getWalletBalance();
      getChannelBalance();
      getTransactions();
    }, 30000); // Update every 30 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <Header user={user} setUser={setUser} />
      <div className="main-content">
        <div className="balance-section">
          <h2>Wallet Balance: {walletBalance} sats</h2>
          <h3>Channel Balance: {channelBalance} sats</h3>
          <h3>Bitcoin Price: ${price}</h3>
        </div>
        <Buttons setModalState={setModalState} />
        <Chart chartData={chartData} />
        <Transactions transactions={transactions} />
      </div>
      <PaymentsModal 
        modalState={modalState} 
        setModalState={setModalState}
        user={user}
        backendUrl={backendUrl}
      />
    </div>
  );
};

export default App;
```

#### axiosWithAuth.js - Authenticated HTTP Client

This utility handles JWT authentication for API requests:

```javascript
import axios from 'axios';

const axiosWithAuth = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  const token = localStorage.getItem('token');

  return axios.create({
    baseURL: backendUrl,
    headers: {
      authorization: token,
    },
  });
};

export default axiosWithAuth;
```

**Key Features:**
- **Automatic Token Inclusion:** Adds JWT token to all requests
- **Base URL Configuration:** Uses environment variable for backend URL
- **Consistent Interface:** Same API as regular Axios but with auth

#### PaymentsModal.js - Invoice and Payment Interface

This component handles both creating invoices and paying them:

```javascript
import React, { useState } from 'react';
import axiosWithAuth from '../utils/axiosWithAuth';

const PaymentsModal = ({ modalState, setModalState, user, backendUrl }) => {
  const [amount, setAmount] = useState('');
  const [invoice, setInvoice] = useState('');
  const [paymentRequest, setPaymentRequest] = useState('');
  const [paymentResult, setPaymentResult] = useState(null);

  // Handle creating an invoice
  const handleReceive = () => {
    axiosWithAuth()
      .post(`${backendUrl}/lightning/invoice`, {
        value: parseInt(amount),
        memo: 'Pleb Wallet Invoice',
        user_id: user.id
      })
      .then(res => {
        setPaymentRequest(res.data.payment_request);
      })
      .catch(err => console.log(err));
  };

  // Handle paying an invoice
  const handleSend = () => {
    axiosWithAuth()
      .post(`${backendUrl}/lightning/pay`, {
        payment_request: invoice,
        user_id: user.id
      })
      .then(res => {
        setPaymentResult(res.data);
      })
      .catch(err => {
        console.log(err);
        alert('Payment failed - you may not have admin permissions');
      });
  };

  // Clear form data
  const clearForm = () => {
    setAmount('');
    setInvoice('');
    setPaymentRequest('');
    setPaymentResult(null);
  };

  if (!modalState) return null;

  return (
    <div className="modal-overlay">
      <div className="modal">
        {modalState === 'receive' && (
          <div>
            <h3>Receive Payment</h3>
            {!paymentRequest ? (
              <div>
                <input
                  type="number"
                  placeholder="Amount in sats"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                />
                <button onClick={handleReceive}>Create Invoice</button>
              </div>
            ) : (
              <div>
                <p>Payment Request:</p>
                <textarea value={paymentRequest} readOnly />
                <button onClick={() => navigator.clipboard.writeText(paymentRequest)}>
                  Copy Invoice
                </button>
              </div>
            )}
          </div>
        )}

        {modalState === 'send' && (
          <div>
            <h3>Send Payment</h3>
            {!paymentResult ? (
              <div>
                <textarea
                  placeholder="Paste lightning invoice here"
                  value={invoice}
                  onChange={(e) => setInvoice(e.target.value)}
                />
                <button onClick={handleSend}>Pay Invoice</button>
              </div>
            ) : (
              <div>
                <p>Payment Successful!</p>
                <p>Amount: {paymentResult.value} sats</p>
                <p>Fees: {paymentResult.fees} sats</p>
              </div>
            )}
          </div>
        )}

        <button onClick={() => {
          setModalState('');
          clearForm();
        }}>
          Close
        </button>
      </div>
    </div>
  );
};

export default PaymentsModal;
```

### Setting Up the Frontend & Backend Preparation

#### Prerequisites

Before setting up the frontend, ensure you have:

1. **Backend Running:** Your Pleb Wallet backend from previous lessons
2. **Lightning Network:** Polar running with your test network
3. **Node.js:** Version 14 or higher
4. **Git:** For cloning the repository

#### Step 1: Clone and Install

```bash
## Clone the updated frontend
git clone https://github.com/plebdevs/pleb-wallet-frontend.git
cd pleb-wallet-frontend

## Install dependencies
npm install
```

#### Step 2: Environment Configuration

Create a `.env` file in the root directory:

```bash
## .env file
REACT_APP_BACKEND_URL=http://localhost:5500
```

**Important Environment Variables:**
- `REACT_APP_BACKEND_URL`: The URL where your backend server is running
- Must start with `REACT_APP_` for React to recognize it
- Use `http://localhost:5500` for local development

#### Step 3: Start the Development Server

```bash
npm start
```

The frontend will start on `http://localhost:3000` and automatically open in your browser.

#### Backend Preparation

Before testing the frontend, ensure your backend is properly configured:

#### Step 1: Update Rate Limiting

The frontend makes frequent API calls, so we need to increase the rate limit:

```javascript
// In index.js, update the rate limiter
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 1000, // Increased from 100 to 1000 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
});
```

#### Step 2: Ensure CORS is Configured

Make sure your backend allows requests from the frontend:

```javascript
// In index.js, ensure CORS is properly configured
app.use(cors({
  origin: ['http://localhost:3000', 'http://localhost:3001'],
  credentials: true
}));
```

#### Step 3: Start All Services

Start your services in this order:

```bash
## Terminal 1: Start Docker Desktop and Polar
## Open Docker Desktop
## Start Polar and your Lightning network

## Terminal 2: Start Backend
cd pleb-wallet-backend
npm run start

## Terminal 3: Start Frontend
cd pleb-wallet-frontend
npm start
```
## System Testing & Data Flow
<chapterId>e99fbaf2-0ed1-42da-9a1a-332a48fe34ca</chapterId>

### Testing the Complete System

Now let's test the entire full-stack application with real user scenarios.

#### Test Scenario 1: New User Registration and Invoice Creation

**Step 1: Create a New User**

1. Open `http://localhost:3000` in your browser
2. Click "Sign Up"
3. Enter username: `testuser`
4. Enter password: `testpass`
5. Click "Sign Up"
6. You should see: "Your user was successfully created, you can now log in"

**Step 2: Login**

1. Click "Login"
2. Enter the same credentials
3. Click "Login"
4. You should see: "Welcome testuser" in the header

**Step 3: Create an Invoice**

1. Click "Receive"
2. Enter amount: `150`
3. Click "Create Invoice"
4. You should see a payment request and QR code

**Step 4: Pay the Invoice (Using Polar)**

1. Copy the payment request
2. Open Polar
3. Click on Bob's node
4. Click "Pay Invoice"
5. Paste the payment request
6. Click "Pay Invoice"
7. Return to the frontend - you should see the payment appear in transactions

#### Test Scenario 2: Admin User Payment Flow

**Step 1: Login as Admin**

1. Logout from the current user
2. Login with admin credentials:
   - Username: `Alice`
   - Password: `pass1`
3. You should see: "Welcome Alice"

**Step 2: Create an Invoice in Polar**

1. Open Polar
2. Click on Bob's node
3. Click "Create Invoice"
4. Set amount: `1000`
5. Set memo: "Test payment to Bob"
6. Click "Create Invoice"
7. Copy the payment request

**Step 3: Pay the Invoice from Frontend**

1. Return to the frontend
2. Click "Send"
3. Paste the payment request
4. Click "Pay Invoice"
5. You should see the payment processed successfully
6. The transaction should appear in your transaction list

#### Test Scenario 3: Permission Testing

**Step 1: Test Regular User Sending (Should Fail)**

1. Login as a regular user (not admin)
2. Try to send a payment
3. You should get an error: "Request failed with status 401"
4. This confirms that only admin users can send payments

**Step 2: Test Regular User Receiving (Should Work)**

1. Create an invoice as a regular user
2. Pay it from Polar
3. The payment should be received successfully
4. This confirms that regular users can receive payments


### Frontend to Backend Communication

```
1. User Action → React Event Handler → API Call
2. API Call → Backend Route → Middleware → Controller
3. Controller → Database/Lightning → Response
4. Response → Frontend State Update → UI Update
```

#### Example: Creating an Invoice

```javascript
// 1. User clicks "Create Invoice"
const handleReceive = () => {
  // 2. Frontend makes API call with JWT token
  axiosWithAuth()
    .post(`${backendUrl}/lightning/invoice`, {
      value: parseInt(amount),
      memo: 'Pleb Wallet Invoice',
      user_id: user.id
    })
    .then(res => {
      // 6. Update frontend state with invoice data
      setPaymentRequest(res.data.payment_request);
    })
    .catch(err => console.log(err));
};

// 3. Backend receives request → authenticate middleware
// 4. Create invoice with LND → Save to database
// 5. Return invoice data to frontend
```

#### Real-time Updates

The frontend polls the backend every 30 seconds for updates:

```javascript
useEffect(() => {
  const interval = setInterval(() => {
    getPrice();           // Bitcoin price from Coinbase
    getWalletBalance();   // On-chain balance from LND
    getChannelBalance();  // Lightning balance from LND
    getTransactions();    // Transaction history from database
  }, 30000);

  return () => clearInterval(interval);
}, []);
```

### Full-Stack Troubleshooting

#### CORS Errors

**Error:** `Access to XMLHttpRequest at 'http://localhost:5500' from origin 'http://localhost:3000' has been blocked by CORS policy`

**Solution:** Ensure CORS is properly configured in your backend:

```javascript
app.use(cors({
  origin: ['http://localhost:3000'],
  credentials: true
}));
```

#### Environment Variable Issues

**Error:** `Cannot read property 'REACT_APP_BACKEND_URL' of undefined`

**Solution:** 
1. Ensure your `.env` file is in the root directory
2. Restart the React development server
3. Check that the variable name starts with `REACT_APP_`

#### Authentication Errors

**Error:** `Request failed with status 401`

**Solution:**
1. Check that you're logged in
2. Verify the JWT token is stored in localStorage
3. Ensure the backend JWT secret matches
4. Check that the user has appropriate permissions

#### Rate Limiting Issues

**Error:** `Too many requests from this IP`

**Solution:** Increase the rate limit in your backend:

```javascript
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 1000, // Increase this number
  message: 'Too many requests from this IP, please try again later.'
});
```

#### Lightning Network Issues

**Error:** `No route found` or `Unable to find path`

**Solution:**
1. Ensure Polar is running
2. Check that nodes have channels with sufficient balance
3. Verify your backend is connected to the correct LND node

## Frontend Optimization & Security
<chapterId>fe4165fe-12c1-4755-b653-f0146b2685fd</chapterId>

### Frontend Customization and Best Practices

The current frontend is a basic template. Here are some enhancement ideas:

#### UI/UX Improvements

**QR Code Generation:**
```javascript
// Add QR code display for invoices
import QRCode from 'qrcode.react';

<QRCode value={paymentRequest} size={200} />
```

**Loading Spinners:**
```javascript
const [loading, setLoading] = useState(false);

const handleReceive = () => {
  setLoading(true);
  axiosWithAuth()
    .post(`${backendUrl}/lightning/invoice`, data)
    .then(res => {
      setPaymentRequest(res.data.payment_request);
      setLoading(false);
    });
};
```

**Real-time Invoice Updates:**
```javascript
// WebSocket connection for real-time payment notifications
useEffect(() => {
  const ws = new WebSocket('ws://localhost:5500');
  
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.type === 'invoice_paid') {
      getTransactions(); // Refresh transactions
    }
  };
}, []);
```

#### Feature Additions

**Transaction Filtering:**
```javascript
const [filter, setFilter] = useState('all');

const filteredTransactions = transactions.filter(tx => {
  if (filter === 'sent') return tx.send;
  if (filter === 'received') return !tx.send;
  return true;
});
```

**Balance History Chart:**
```javascript
// Store balance history in database
const [balanceHistory, setBalanceHistory] = useState([]);

// Update chart with balance over time instead of just price
```

**Invoice Expiration:**
```javascript
// Add expiration time to invoices
const [expirationTime, setExpirationTime] = useState(null);

useEffect(() => {
  if (paymentRequest) {
    const timer = setTimeout(() => {
      setPaymentRequest('');
      alert('Invoice expired');
    }, 600000); // 10 minutes

    return () => clearTimeout(timer);
  }
}, [paymentRequest]);
```

#### Responsive Design

The current frontend works on desktop but could be improved for mobile:

```css
/* Add responsive breakpoints */
@media (max-width: 768px) {
  .main-content {
    flex-direction: column;
  }
  
  .chart-container {
    width: 100%;
    height: 300px;
  }
  
  .modal {
    width: 90%;
    max-width: 400px;
  }
}
```


#### Frontend Security Best Practices

**Token Storage:**
```javascript
// Consider using secure storage for JWT tokens
// Current: localStorage (simple but less secure)
// Better: httpOnly cookies or secure storage libraries
```

**Input Validation:**
```javascript
const validateAmount = (amount) => {
  const num = parseInt(amount);
  if (isNaN(num) || num <= 0) {
    throw new Error('Invalid amount');
  }
  return num;
};
```

**Error Handling:**
```javascript
// Don't expose sensitive error details to users
.catch(err => {
  console.log(err); // Log for debugging
  alert('Payment failed. Please try again.'); // Generic user message
});
```

#### API Call Optimization

**Batch Requests:**
```javascript
// Instead of multiple individual calls
const getInitialData = async () => {
  const [price, balance, channelBalance, transactions] = await Promise.all([
    fetch('https://api.coinbase.com/v2/exchange-rates?currency=BTC'),
    axiosWithAuth().get(`${backendUrl}/lightning/balance`),
    axiosWithAuth().get(`${backendUrl}/lightning/channelbalance`),
    axiosWithAuth().get(`${backendUrl}/lightning/invoices`)
  ]);
  
  // Process all responses together
};
```

**Smart Polling:**
```javascript
// Only poll when tab is active
useEffect(() => {
  const handleVisibilityChange = () => {
    if (document.hidden) {
      clearInterval(pollInterval);
    } else {
      startPolling();
    }
  };
  
  document.addEventListener('visibilitychange', handleVisibilityChange);
  return () => document.removeEventListener('visibilitychange', handleVisibilityChange);
}, []);
```

### Testing the Full Stack

Here's a comprehensive test checklist:

#### Basic Functionality Tests

- [ ] Frontend loads without errors
- [ ] Bitcoin price displays correctly
- [ ] Wallet balances display correctly
- [ ] Transaction history displays correctly

#### Authentication Tests

- [ ] User can sign up
- [ ] User can log in
- [ ] User can log out
- [ ] JWT token is stored and used correctly
- [ ] Protected routes work properly

#### Lightning Functionality Tests

- [ ] User can create invoices
- [ ] Invoices can be paid externally (via Polar)
- [ ] Payments appear in transaction history
- [ ] Admin users can pay invoices
- [ ] Regular users cannot pay invoices
- [ ] Invoice amounts are correct
- [ ] Transaction details are accurate

#### Error Handling Tests

- [ ] Invalid login credentials show error
- [ ] Network errors are handled gracefully
- [ ] Invalid payment requests show error
- [ ] Insufficient balance errors work
- [ ] Rate limiting works correctly

#### Performance Tests

- [ ] Page loads quickly
- [ ] API calls complete in reasonable time
- [ ] Chart renders smoothly
- [ ] Modal interactions are responsive

### Deployment Considerations

While we'll cover deployment in the next lesson, here are some frontend deployment considerations:

#### Environment Variables for Production

```bash
## Production .env
REACT_APP_BACKEND_URL=https://your-backend-domain.com
REACT_APP_ENVIRONMENT=production
```

#### Build Optimization

```bash
## Create production build
npm run build

## This creates a 'build' folder with optimized static files
```

#### Hosting Options

**Static Site Hosting:**
- Vercel (recommended)
- Netlify
- GitHub Pages
- AWS S3 + CloudFront

**Server-Side Rendering:**
- Next.js (if converting to SSR)
- Gatsby (for static generation)

### Key Takeaways for Frontend Optimization

1. **Full-Stack Integration:** Successfully connecting frontend and backend requires careful attention to CORS, authentication, and API contracts
2. **Real-time Updates:** User interfaces need to stay synchronized with backend state through polling or WebSockets
3. **Error Handling:** Robust error handling is crucial for good user experience
4. **Security:** Frontend security depends on proper token handling and input validation
5. **Performance:** Optimize API calls and use smart polling to reduce server load
6. **Testing:** Comprehensive testing ensures all user flows work correctly
7. **Customization:** The basic template can be extensively customized for your specific needs

#### Practice Exercises and Resources

1. **Add QR Code Generation:**
   - Install a QR code library
   - Display QR codes for generated invoices
   - Add click-to-copy functionality

2. **Implement Real-time Updates:**
   - Add WebSocket connection to backend
   - Update UI immediately when invoices are paid
   - Show live payment notifications

3. **Enhanced Transaction Display:**
   - Add transaction filtering (sent/received)
   - Implement pagination for large transaction lists
   - Add transaction search functionality

4. **Mobile Responsiveness:**
   - Improve mobile layout
   - Add touch-friendly interactions
   - Optimize for different screen sizes

5. **Advanced Features:**
   - Add invoice expiration countdown
   - Implement balance history chart
   - Add user profile management



#### Frontend Development
- [React Documentation](https://react.dev/) - Complete React reference
- [Axios Documentation](https://axios-http.com/) - HTTP client library
- [React Router](https://reactrouter.com/) - For multi-page applications

#### Lightning Development
- [Lightning Network Specifications](https://github.com/lightning/bolts) - Technical specs
- [LND API Reference](https://lightning.engineering/api-docs/) - Complete API documentation
- [Lightning Design Guidelines](https://lightning.engineering/guides/) - Best practices

#### Deployment Resources
- [Vercel Documentation](https://vercel.com/docs) - Frontend deployment
- [Netlify Documentation](https://docs.netlify.com/) - Alternative hosting
- [React Build Process](https://create-react-app.dev/docs/production-build/) - Production optimization

#### Security Resources
- [OWASP JavaScript Security](https://owasp.org/www-project-top-ten/) - Security best practices
- [JWT Best Practices](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/) - Token security
- [React Security](https://pragmaticwebsecurity.com/articles/spasecurity.html) - Frontend security guide

You've now completed the full backend course! Your Lightning wallet application is functional, tested, and ready for deployment. The next lesson will take you through deploying everything to production, making your application accessible to users worldwide.

Remember: This is just the beginning. The patterns and techniques you've learned here can be applied to build any Lightning-enabled application. The Lightning ecosystem is growing rapidly, and you're now equipped to be part of that growth! 


# Production Deployment
<partId>ccc611f9-4369-4e18-a096-758cde12a97b</partId>

## Lesson 13: Deploy Your Production Database and Node
<chapterId>f2f066a1-63a5-4a8a-9d92-32ba07d8a645</chapterId>


**Warning:** We'll be dealing with real money and real Lightning networks in this lesson. We'll discuss security considerations and provide options for using testnet vs mainnet.

### Pre-Deployment Assessment

Congratulations on making it this far! Let's recap what we've accomplished:

- ✅ **Express Server:** RESTful API with proper routing and middleware
- ✅ **Database System:** SQLite with Knex.js migrations and seeds
- ✅ **Lightning Integration:** LND connection with invoice/payment functionality
- ✅ **Authentication:** JWT-based auth with admin permissions
- ✅ **Database Models:** Clean abstraction layer for data operations
- ✅ **API Testing:** Complete endpoints tested with Postman/Insomnia
- ✅ **Frontend Integration:** React app connected to backend

Now we're ready to take this entire system live and make it accessible to the world!

Before we dive into deployment, let's discuss some important considerations:

#### Security Considerations

**Real Money Risk:**
- Your node and app will be susceptible to attacks
- The app has admin rights to your node, so funds could be stolen
- Consider using testnet for learning/portfolio purposes
- Use small amounts if deploying to mainnet

**Privacy Concerns:**
- The wallet activity isn't private unless you update the backend
- API endpoints like `/lightning/invoices` are publicly accessible
- Consider implementing proper access controls

**Potential Vulnerabilities:**
- This is an educational project, not production-ready
- There may be security flaws and attack vectors
- Always tread carefully with real funds

#### Cost Considerations

**Monthly Costs:**
- Server hosting: ~$7/month (Heroku basic dyno)
- Database hosting: ~$5/month (Heroku Postgres)
- Lightning node: ~$12/month (Voltage light node)
- Frontend hosting: Free (Vercel)

**Total:** ~$24/month for a complete Lightning wallet infrastructure

**Free Alternatives:**
- Use testnet instead of mainnet
- Use Heroku's built-in SQLite (resets every 24 hours)
- Consider if deployment is necessary for your goals

#### Goal Assessment

Ask yourself:
- Are you trying to show off a mainnet wallet?
- Does testnet suffice for your portfolio?
- Do you need it live and deployed?
- Could a local demo video be enough?

### Deploying Backend to Heroku

Heroku is a cloud platform service that allows developers to deploy, manage, and scale applications without a lot of overhead. It abstracts away the complexities of managing servers, infrastructure, and databases, allowing you to focus purely on the code.

**Key Features:**
- **Platform as a Service (PaaS):** Provides both environment and infrastructure
- **Simple Deployment:** Deploy with Git push
- **Multiple Languages:** Supports Node.js, Ruby, Java, Python, and more
- **Dynos:** Containerized instances that run your application
- **Add-ons:** Marketplace of services (databases, email, etc.)
- **Scalability:** Easy scaling as your app grows

**Why Heroku for Beginners:**
- Optimized for ease of use
- Consistent performance
- Easy to set up and scale
- Great for first-time deployments

#### Step 1: Create a New Heroku App

First, create a Heroku account and set up a new application:

1. Go to [heroku.com](https://heroku.com) and sign up
2. Click "New" → "Create new app"
3. Name your app: `pleb-wallet-backend` (or similar)
4. Choose your region
5. Click "Create app"

#### Step 2: Connect Your Backend Repository

1. Go to the "Deploy" tab
2. Select "GitHub" as deployment method
3. Connect your GitHub account
4. Search for your `pleb-wallet-backend` repository
5. Click "Connect"

#### Step 3: Initial Deployment

Deploy immediately to test basic functionality:

1. Click "Deploy Branch" (master/main)
2. Watch the build logs
3. Once complete, click "Open app"
4. You should see: "I'm alive" message

**Expected URL format:** `https://your-app-name.herokuapp.com/`

#### Step 4: Enable Web Dyno

Ensure your server stays persistently online:

1. Go to "Resources" tab
2. Toggle the web dyno to "ON"
3. This will cost ~$7/month but keeps your server running

#### Step 5: Add Environment Variables

1. Go to "Settings" tab
2. Click "Reveal Config Vars"
3. Add these initial variables:

```
ADMIN_KEY=1234
JWT_SECRET=your-secure-secret-here
NODE_ENV=development
```

**Important:** Use secure secrets for production!

#### Step 6: Test Basic Functionality

Test user creation and authentication:

```bash
## Create a user
POST https://your-app-name.herokuapp.com/users/register
{
  "username": "testuser",
  "password": "password123"
}

## Login
POST https://your-app-name.herokuapp.com/users/login
{
  "username": "testuser",
  "password": "password123"
}

## Get all users (requires admin token)
GET https://your-app-name.herokuapp.com/users
Authorization: your-jwt-token
```

### Adding PostgreSQL Database

#### Step 7: Add Postgres Buildpack

1. Go to "Resources" tab
2. Search for "Heroku Postgres"
3. Select the basic plan (~$5/month)
4. Click "Submit Order Form"

Heroku will automatically add a `DATABASE_URL` environment variable.

#### Step 8: Update Environment Variables

Change your environment to production:

```
NODE_ENV=production
```

#### Step 9: Run Database Migrations

1. Go to "More" → "Run console"
2. Run the migration command:

```bash
npx knex migrate:latest
```

This will create your production database tables.

#### Step 10: Test Production Database

Create and test a production user:

```bash
## Create admin user
POST https://your-app-name.herokuapp.com/users/register
{
  "username": "admin",
  "password": "securepassword",
  "admin_key": "1234"
}

## Login and get users
POST https://your-app-name.herokuapp.com/users/login
GET https://your-app-name.herokuapp.com/users
```

### Common Deployment Errors

#### Express Rate Limit Error

**Error:** `express-rate-limit` warning about reverse proxy

**Fix:** Add this to your `index.js`:

```javascript
// Add this line to trust the first proxy
app.set('trust proxy', 1);
```

#### DateTime Field Error

**Error:** `date/time field value out of range`

**Fix:** Update your `lnd.js` file:

```javascript
// If the invoice exists, update it in the database
if (existingInvoice) {
  const settleDate = new Date(data.settle_date * 1000).toISOString();
  await Invoice.update(data.payment_request, {
    settled: data.settled,
    settle_date: settleDate,
  });
} else {
  console.log("Invoice not found in the database");
}
```

#### PostgreSQL SSL Error

**Error:** `no pg_hba.conf entry for host`

**Fix:** Update your `knexfile.js` production config:

```javascript
production: {
  client: "pg",
  connection: {
    connectionString: process.env.DATABASE_URL,
    ssl: { rejectUnauthorized: false },
  },
  migrations: {
    directory: "./db/migrations",
  },
  seeds: {
    directory: "./db/seeds",
  },
},
```

## Launching the Wallet Stack
<chapterId>ecfef4ea-e2f8-484b-9bc3-b1522506c29f</chapterId>

### Deploying Lightning Node with Voltage

#### What is Voltage?

Voltage is a cloud-based Lightning node hosting service that makes it easy to deploy and manage Lightning nodes without dealing with infrastructure.

**Why Voltage:**
- Easiest Lightning node deployment
- No hardware management
- Encrypted cloud storage
- Great for development and side projects

#### Step 11: Create a Voltage Node

1. Go to [nodes.voltage.cloud](https://nodes.voltage.cloud)
2. Create an account
3. Click "Create Node"
4. Choose "LND" as your implementation
5. Select "Lite Node" (~$12/month)
6. Choose network: **mainnet** or **testnet**
7. Create username and password (write them down!)
8. Wait for node initialization

#### Step 12: Get Free Inbound Channel

Voltage offers a free inbound channel to new users:

1. Look for the popup on your node dashboard
2. Click "Request Free Channel"
3. This gives you 500,000 sats inbound capacity
4. Allows immediate receiving from the Lightning network

#### Step 13: Connect Node to Server

We'll use LND Connect URI instead of separate host/cert/macaroon variables.

**Update your `lnd.js` file:**

```javascript
const options = {
  // Replace the individual connection options with LND Connect URI
  lndConnectUri: process.env.LND_CONNECT_URI,
};
```

**Get your LND Connect URI:**

1. Go to your Voltage node dashboard
2. Click "Connect" → "LND Connect"
3. Copy the long URI string

**Add to Heroku environment variables:**

```
LND_CONNECT_URI=lndconnect://your-long-uri-string-here
```

#### Step 14: Deploy and Test Lightning Connection

1. Deploy your updated code to Heroku
2. Watch the logs - you should see: "LND gRPC connection state is active"
3. Test a Lightning endpoint:

```bash
GET https://your-app-name.herokuapp.com/lightning/channelbalance
```

You should see your Lightning channel balance!

### Frontend Deployment with Vercel

#### Step 15: Deploy Frontend

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "New Project"
4. Import your `pleb-wallet-frontend` repository
5. Add environment variable:

```
REACT_APP_BACKEND_URL=https://your-app-name.herokuapp.com
```

**Important:** Don't add a trailing slash!

6. Click "Deploy"

#### Step 16: Test Frontend Connection

1. Visit your Vercel deployment URL
2. You should see:
   - Bitcoin price loading
   - Wallet balance displaying
   - Transaction history (empty initially)


#### Test Scenario 1: Non-Admin User Receiving Payment

1. **Create regular user:**
   - Sign up through frontend
   - Username: `testuser`
   - Password: `password123`

2. **Generate invoice:**
   - Click "Receive"
   - Enter amount: `100`
   - Click "Create Invoice"

3. **Pay invoice externally:**
   - Use another Lightning wallet (Phoenix, Alby, etc.)
   - Pay the generated invoice
   - Watch transaction appear in frontend

#### Test Scenario 2: Admin User Sending Payment

1. **Create admin user:**
   ```bash
   POST https://your-app-name.herokuapp.com/users/register
   {
     "username": "admin",
     "password": "securepassword",
     "admin_key": "your-secure-admin-key"
   }
   ```

2. **Login as admin:**
   - Use frontend to login
   - Should see "Welcome admin"

3. **Send payment:**
   - Get invoice from external wallet
   - Click "Send" in frontend
   - Paste invoice and pay
   - Payment should complete successfully

#### Test Scenario 3: Permission Verification

1. **Login as regular user**
2. **Try to send payment**
3. **Should fail with 401 error**
4. **Confirms admin-only sending works**

### Security Hardening & Monitoring

#### Step 17: Secure Your Secrets

**Update environment variables with secure values:**

```bash
## Generate secure admin key
openssl rand -base64 32

## Generate secure JWT secret
openssl rand -base64 64
```

**Add to Heroku:**
```
ADMIN_KEY=your-secure-32-char-key
JWT_SECRET=your-secure-64-char-secret
```

#### API Security Improvements

**Rate limiting adjustments:**

```javascript
// Increase rate limit for frontend polling
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 1000, // Increased from 100
  message: 'Too many requests from this IP, please try again later.'
});
```

**CORS configuration:**

```javascript
app.use(cors({
  origin: ['https://your-frontend-domain.vercel.app'],
  credentials: true
}));
```


#### Monthly Costs Breakdown

**Required Services:**
- Heroku Web Dyno: $7/month
- Heroku Postgres: $5/month
- Voltage Lightning Node: $12/month
- Vercel Frontend: Free

**Total: $24/month**

#### Cost-Saving Options

**Use Testnet:**
- Same functionality, no real money risk
- Perfect for portfolios and learning

**Heroku Eco Plan:**
- Sleep after 30 minutes of inactivity
- Fine for demo purposes

**Alternative Hosting:**
- Railway: Cheaper alternatives
- Digital Ocean: More control, similar cost
- AWS/GCP: More complex but potentially cheaper

### Monitoring and Maintenance

#### Heroku Logs

Monitor your application:

```bash
## View live logs
heroku logs --tail --app your-app-name

## View specific number of lines
heroku logs -n 200 --app your-app-name
```

#### Voltage Monitoring

Monitor your Lightning node:

1. Use Voltage dashboard
2. Set up ThunderHub dashboard
3. Monitor channel balance and connectivity

#### Database Monitoring

Monitor your database:

1. Heroku Postgres dashboard
2. View connection counts
3. Monitor query performance

#### Troubleshooting Common Issues

##### Frontend Can't Connect to Backend

**Check:**
- Environment variable spelling
- No trailing slashes in URLs
- CORS configuration
- Heroku dyno is running

##### Lightning Node Connection Issues

**Check:**
- LND_CONNECT_URI is correct
- Node is running on Voltage
- Network connectivity
- Firewall issues

##### Database Connection Problems

**Check:**
- DATABASE_URL is set
- SSL configuration
- Migration status
- Connection limits

##### Payment Failures

**Check:**
- Channel liquidity
- Node connectivity
- Invoice validity
- Admin permissions

### Reliability: Optimization & Backups

#### Database Optimization

**Connection Pooling:**

```javascript
// In knexfile.js
pool: {
  min: 2,
  max: 10,
  acquireTimeoutMillis: 30000,
  idleTimeoutMillis: 30000
}
```

**Query Optimization:**
- Add database indexes
- Optimize N+1 queries
- Use database views for complex queries

#### API Optimization

**Response Caching:**

```javascript
// Add simple caching for price data
const cache = new Map();
const CACHE_DURATION = 30000; // 30 seconds

app.get('/api/price', (req, res) => {
  const cached = cache.get('btc-price');
  if (cached && Date.now() - cached.timestamp < CACHE_DURATION) {
    return res.json(cached.data);
  }
  
  // Fetch fresh data and cache it
  // ... price fetching logic
});
```

## Optimizing the Wallet Stack
<chapterId>4132c2e3-3078-4356-8207-d094584dbfd5</chapterId>

### Advanced Deployment Features

#### Automatic Deployments

Set up automatic deployments:

1. Go to Heroku Deploy tab
2. Enable "Automatic deploys"
3. Choose "Wait for CI to pass"
4. Every push to main triggers deployment

#### Environment-Specific Configurations

Create staging environment:

```javascript
// config/environments.js
const environments = {
  development: {
    host: 'localhost:5500',
    logLevel: 'debug'
  },
  staging: {
    host: 'your-staging-app.herokuapp.com',
    logLevel: 'info'
  },
  production: {
    host: 'your-production-app.herokuapp.com',
    logLevel: 'error'
  }
};

module.exports = environments[process.env.NODE_ENV];
```

#### Health Checks

Add health check endpoint:

```javascript
app.get('/health', async (req, res) => {
  try {
    // Check database connection
    await knex.raw('SELECT 1');
    
    // Check Lightning node connection
    const info = await lnd.getInfo({});
    
    res.json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      services: {
        database: 'connected',
        lightning: 'connected',
        node_pubkey: info.identity_pubkey.slice(0, 10) + '...'
      }
    });
  } catch (error) {
    res.status(500).json({
      status: 'unhealthy',
      error: error.message
    });
  }
});
```

### Backup and Recovery

#### Database Backups

Heroku automatically backs up Postgres:

```bash
## Create manual backup
heroku pg:backups:capture --app your-app-name

## List backups
heroku pg:backups --app your-app-name

## Download backup
heroku pg:backups:download --app your-app-name
```

#### Lightning Node Backups

Voltage handles node backups automatically, but you should:

1. Save your node credentials securely
2. Export channel backup file
3. Store seed phrase safely

#### Code Backups

Ensure your code is backed up:

1. Multiple Git remotes
2. Regular commits
3. Tagged releases

### What's Next?

Congratulations! You've successfully deployed a complete Lightning wallet system. Here are some next steps:

#### Immediate Improvements

1. **Add more security features:**
   - Rate limiting per user
   - Input validation
   - SQL injection protection
   - XSS protection

2. **Enhance user experience:**
   - Real-time WebSocket updates
   - Better error handling
   - Loading states
   - Offline support

3. **Add new features:**
   - Lightning Address support
   - Recurring payments
   - Multi-user support
   - Invoice templates

#### Advanced Topics

1. **Scaling:**
   - Load balancing
   - Database sharding
   - CDN integration
   - Caching strategies

2. **Monitoring:**
   - Application metrics
   - Error tracking
   - Performance monitoring
   - Alerting systems

3. **DevOps:**
   - CI/CD pipelines
   - Infrastructure as code
   - Container orchestration
   - Blue-green deployments

### Key Takeaways and Resources

1. **Deployment is a Process:** Deploying to production involves many steps and considerations beyond just running code

2. **Security is Paramount:** Always prioritize security, especially when dealing with real money and Lightning networks

3. **Testing is Critical:** Thoroughly test each component and integration point in production

4. **Monitoring is Essential:** Set up proper monitoring and logging from day one

5. **Start Small:** Begin with testnet and small amounts before scaling up

6. **Documentation Matters:** Keep detailed records of your deployment process and configurations

7. **Backup Everything:** Have backup strategies for your database, node, and code

8. **Plan for Costs:** Understand the ongoing costs and plan accordingly

#### Practice Exercises

1. **Deploy to Testnet:**
   - Create a testnet version of your entire stack
   - Practice the deployment process without risk

2. **Implement Health Checks:**
   - Add comprehensive health check endpoints
   - Set up monitoring alerts

3. **Add Security Features:**
   - Implement API key authentication
   - Add request validation
   - Set up HTTPS redirects

4. **Create a Staging Environment:**
   - Set up a staging deployment
   - Practice blue-green deployments

5. **Implement Backup Strategy:**
   - Set up automated database backups
   - Create disaster recovery procedures


#### Deployment Platforms
- [Heroku Documentation](https://devcenter.heroku.com/) - Complete deployment guide
- [Vercel Documentation](https://vercel.com/docs) - Frontend deployment
- [Railway](https://railway.app/) - Alternative to Heroku
- [Digital Ocean App Platform](https://www.digitalocean.com/products/app-platform/) - Another alternative

#### Lightning Node Services
- [Voltage](https://voltage.cloud/) - Managed Lightning nodes
- [Umbrel](https://umbrel.com/) - Self-hosted Lightning node
- [Start9](https://start9.com/) - Personal server OS
- [RaspiBlitz](https://github.com/rootzoll/raspiblitz) - DIY Lightning node

#### Security Resources
- [OWASP API Security](https://owasp.org/www-project-api-security/) - API security best practices
- [Node.js Security Checklist](https://blog.risingstack.com/node-js-security-checklist/) - Security guidelines
- [Lightning Security](https://github.com/lightningnetwork/lnd/blob/master/docs/safety.md) - Lightning security guide

#### Monitoring Tools
- [Heroku Metrics](https://devcenter.heroku.com/articles/metrics) - Application monitoring
- [Sentry](https://sentry.io/) - Error tracking
- [DataDog](https://www.datadoghq.com/) - Comprehensive monitoring
- [New Relic](https://newrelic.com/) - Application performance monitoring

#### Learning Resources
- [The Twelve-Factor App](https://12factor.net/) - Methodology for building SaaS apps
- [Lightning Network Specifications](https://github.com/lightning/bolts) - Technical specifications
- [LND Developer Documentation](https://docs.lightning.engineering/) - LND-specific guides

### Final Thoughts

You've just completed an incredible journey! From learning basic JavaScript to deploying a complete Lightning wallet system, you've covered:

- **Backend Development:** Express.js, APIs, middleware
- **Database Management:** SQL, migrations, data modeling
- **Authentication:** JWT tokens, authorization
- **Lightning Network:** Payment processing, node management
- **Frontend Integration:** React, API consumption
- **DevOps:** Cloud deployment, monitoring, security

You're now equipped to build Lightning-enabled applications and have hands-on experience with the entire development lifecycle. The Lightning Network is rapidly growing, and you're now positioned to be part of that growth.

Remember: This is just the beginning. The skills you've learned here can be applied to build any Lightning-enabled application. Keep experimenting, keep learning, and most importantly, keep building!

**Welcome to the Lightning developer community!** 🚀⚡️

---

**Course Complete!** You've successfully completed the PlebDevs Backend Course. Join our Discord community to connect with other developers, share your projects, and continue learning together. 

# Final Section
<partId>b38f3cc6-b123-4c02-b06f-5d417cf81292</partId>


## Reviews & Ratings
<chapterId>1f8e49bd-352a-4be0-890f-913a280f48f4</chapterId>


<isCourseReview>true</isCourseReview>

## Final Exam
<chapterId>5f2fa946-9fb7-4304-95a6-c6d4a3de51e2</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusion
<chapterId>5583a662-6717-4f7c-91a0-576001793ed3</chapterId>

<isCourseConclusion>true</isCourseConclusion>
