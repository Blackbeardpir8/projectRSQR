document.addEventListener("DOMContentLoaded", function () {
    // Base
        // Mobile menu toggle
        document.getElementById('mobile-menu').addEventListener('click', function() {
            document.body.classList.toggle('menu-open');
        });
        
        // Hide header on scroll down, show on scroll up
        let lastScrollTop = 0;
        window.addEventListener('scroll', function() {
            let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
            if (currentScroll > lastScrollTop && currentScroll > 100) {
                // Scrolling down
                document.getElementById('navbar').classList.add('header-hidden');
            } else {
                // Scrolling up
                document.getElementById('navbar').classList.remove('header-hidden');
            }
            lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
        }, false);
// End Base
    
    // Register User
    const registerForm = document.getElementById("registerForm");
    if (registerForm) {
        registerForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            
            const data = {
                first_name: document.getElementById("first_name").value,
                middle_name: document.getElementById("middle_name").value,
                last_name: document.getElementById("last_name").value,
                email: document.getElementById("email").value,
                phone: document.getElementById("phone").value,
                password: document.getElementById("password").value,
                role: document.getElementById("role").value
            };

            const response = await fetch("http://127.0.0.1:8000/api/users/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            if (response.ok) {
                alert("User registered successfully!");
                window.location.href = "login.html";
            } else {
                alert("Error: " + JSON.stringify(result));
            }
        });
    }

    // Login User
    const loginForm = document.getElementById("loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            
            const data = {
                email: document.getElementById("login_email").value,
                password: document.getElementById("login_password").value
            };

            const response = await fetch("http://127.0.0.1:8000/api/users/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            if (response.ok) {
                alert("Login successful!");
                localStorage.setItem("access_token", result.access_token);
                localStorage.setItem("refresh_token", result.refresh_token);
                window.location.href = "dashboard.html";
            } else {
                alert("Error: " + JSON.stringify(result));
            }
        });
    }
});



