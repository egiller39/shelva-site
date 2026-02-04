// Shared Mobile Menu JavaScript
// This file handles the mobile navigation menu functionality for all pages

(function() {
    'use strict';
    
    // Function to check if we're on mobile or tablet
    function isMobile() {
        const width = window.innerWidth;
        return width <= 1200;
    }
    
    // Function to create mobile menu
    function createMobileMenu() {
        const mobileMenuButton = document.querySelector('.nav_mobile-menu-button');
        
        // Always create menu if button exists - CSS handles visibility
        if (!mobileMenuButton) {
            return;
        }
        
        // Check if menu already exists
        let customMenu = document.querySelector('.custom-mobile-menu');
        if (customMenu) {
            return; // Menu already exists
        }
        
        // Create custom mobile menu
        customMenu = document.createElement('div');
        customMenu.className = 'custom-mobile-menu';
        customMenu.innerHTML = `
            <div class="custom-mobile-menu-content">
                <ul class="custom-mobile-menu-list">
                    <li class="custom-mobile-menu-item">
                        <a href="/" class="custom-mobile-menu-link">Home</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/how-it-works" class="custom-mobile-menu-link">How It Works</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/pricing" class="custom-mobile-menu-link">Pricing</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/starter-kit" class="custom-mobile-menu-link">Starter Kit</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/features" class="custom-mobile-menu-link">Features</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/contact" class="custom-mobile-menu-link">Contact</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/release-notes" class="custom-mobile-menu-link">Release Notes</a>
                    </li>
                    <li class="custom-mobile-menu-item">
                        <a href="/policy" class="custom-mobile-menu-link">Policy</a>
                    </li>
                </ul>
            </div>
        `;
        
        document.body.appendChild(customMenu);
        
        // Remove any existing click handlers - clone button to remove all listeners
        const oldButton = mobileMenuButton;
        const newButton = oldButton.cloneNode(true);
        oldButton.parentNode.replaceChild(newButton, oldButton);
        const mobileMenuButtonClean = newButton;
        
        // Ensure button is clickable
        mobileMenuButtonClean.style.cursor = 'pointer';
        mobileMenuButtonClean.style.pointerEvents = 'auto';
        
        // Function to toggle menu
        function toggleMenu(e) {
            if (e) {
                e.preventDefault();
                e.stopPropagation();
                e.stopImmediatePropagation();
            }
            
            if (customMenu.classList.contains('show')) {
                customMenu.classList.remove('show');
                customMenu.style.display = 'none';
                document.body.style.overflow = '';
            } else {
                customMenu.style.display = 'block';
                setTimeout(() => {
                    customMenu.classList.add('show');
                }, 10);
                document.body.style.overflow = 'hidden';
            }
        }
        
        // Remove Webflow's w--open class handler
        mobileMenuButtonClean.classList.remove('w--open');
        
        // Disable Webflow's default navigation behavior
        if (mobileMenuButtonClean.hasAttribute('data-w-id')) {
            mobileMenuButtonClean.removeAttribute('data-w-id');
        }
        
        // Add our handler with capture phase to intercept before Webflow
        mobileMenuButtonClean.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            e.stopImmediatePropagation();
            toggleMenu(e);
            return false;
        }, true);
        
        // Also add in bubble phase as backup
        mobileMenuButtonClean.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            e.stopImmediatePropagation();
            return false;
        }, false);
        
        // Handle touch events for mobile/tablet
        mobileMenuButtonClean.addEventListener('touchend', function(e) {
            e.preventDefault();
            toggleMenu(e);
        }, false);
        
        // Close menu when clicking outside
        customMenu.addEventListener('click', function(e) {
            if (e.target === customMenu) {
                customMenu.classList.remove('show');
                setTimeout(() => {
                    customMenu.style.display = 'none';
                }, 300);
                document.body.style.overflow = '';
            }
        });
        
        // Detect current page and highlight active menu item
        const currentPath = window.location.pathname;
        const menuLinks = customMenu.querySelectorAll('.custom-mobile-menu-link');
        menuLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            // Check if this link matches the current page
            if (linkPath === currentPath || 
                (currentPath === '/' && linkPath === '/') ||
                (currentPath !== '/' && currentPath.startsWith(linkPath) && linkPath !== '/')) {
                link.classList.add('active');
            }
            
            // Close menu when clicking on a link
            link.addEventListener('click', function() {
                customMenu.classList.remove('show');
                setTimeout(() => {
                    customMenu.style.display = 'none';
                }, 300);
                document.body.style.overflow = '';
            });
        });
        
        // Close menu on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && customMenu.classList.contains('show')) {
                customMenu.classList.remove('show');
                setTimeout(() => {
                    customMenu.style.display = 'none';
                }, 300);
                document.body.style.overflow = '';
            }
        });
    }
    
    // Initialize - wait for DOM and Webflow to load
    function initMobileMenu() {
        // Wait a bit for Webflow to finish initializing
        setTimeout(function() {
            createMobileMenu();
        }, 100);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            initMobileMenu();
        });
    } else {
        initMobileMenu();
    }
    
    // Also try after a delay to catch late-loading elements
    setTimeout(function() {
        createMobileMenu();
    }, 500);
    
    // Handle window resize - use debouncing to avoid multiple rapid calls
    let resizeTimeout;
    window.addEventListener('resize', function() {
        // Clear previous timeout
        if (resizeTimeout) {
            clearTimeout(resizeTimeout);
        }
        
        // Debounce resize handler
        resizeTimeout = setTimeout(function() {
            // Remove existing mobile menu if it exists
            const existingMenu = document.querySelector('.custom-mobile-menu');
            if (existingMenu) {
                existingMenu.remove();
            }
            
            // Recreate menu if button exists (CSS will show/hide as needed)
            const button = document.querySelector('.nav_mobile-menu-button');
            if (button) {
                // Small delay to ensure DOM is ready
                setTimeout(function() {
                    createMobileMenu();
                }, 150);
            }
        }, 250); // Debounce delay
    });
})();
