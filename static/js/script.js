function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var loginStatus = document.getElementById("loginStatus");

    // Check login credentials (you may replace this with actual authentication logic)
    if (username === "demo" && password === "password") {
        loginStatus.innerHTML = "Login successful!";
        // Redirect to the challenges page
        window.location.href = "challenges.html";
    } else {
        loginStatus.innerHTML = "Invalid username or password. Please try again.";
    }
}

// script.js

function submitCode() {
    // Replace this with the actual solution for the challenge
    var correctSolution = 'function addNumbers(a, b) { return a + b; }';

    // Get the user's input from the textarea
    var userCode = document.getElementById('code').value;

    // Check if the user's input matches the correct solution
    if (userCode.trim() === correctSolution.trim()) {
        // Redirect to output.html with the message "Correct"
        window.location.href = '/output?result=Correct';
    } else {
        // Redirect to output.html with the message "Incorrect"
        window.location.href = '/output?result=Incorrect';
    }
}

function goBack() {
    // Redirect back to the most recent challenges screen
    window.history.back();
}




// script.js




