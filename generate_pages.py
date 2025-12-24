#!/usr/bin/env python3
"""
Mass page generator for Shelva marketing site
Generates all marketing pages from a template with content variations
"""

import os
import re
from pathlib import Path

# Template content
TEMPLATE_PATH = "site/template.html"

# Page definitions with content
PAGES = {
    "index.html": {
        "title": "Digital Shelf Labels for Shopify",
        "description": "Connect your Shopify store to digital shelf labels. Update prices, inventory, and promotions instantly—no manual work required.",
        "active_nav": "HOME_ACTIVE",
        "content": """
        <header class="section max-height_100vh_desktop overflow_hidden flex_horizontal is-y-center is-accent-primary">
            <div class="container is-max">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-large">
                    <div class="header max-width_small">
                        <h1 class="heading_h1">Sync your shelves. Simplify retail.</h1>
                        <p class="subheading">Connect your Shopify store to digital shelf labels. Update prices, inventory, and promotions instantly—no manual work required.</p>
                        <div class="w-layout-hflex flex-block">
                            <a href="https://apps.shopify.com/shelva-app" target="_blank" class="button on-accent-primary w-button">Install now</a>
                            <img src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68a9397fb13945731c2eb2ce_shopify_logo_white.png" loading="lazy" alt="" class="image-4"/>
                        </div>
                    </div>
                    <div class="w-layout-grid grid_2-col gap-small">
                        <div class="position_relative overflow_hidden">
                            <div class="ix_marquee-vertical-down">
                                <div class="w-layout-grid grid_1-col gap-small padding-top_small">
                                    <div class="image-ratio_3x2">
                                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c43406f6b8a43d00f1b_1.png" width="367" height="244" alt="Retail setting" loading="lazy"/>
                                    </div>
                                    <div class="image-ratio_3x2">
                                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c44bede78afd28e3958_3.png" width="367" height="244" alt="Appointment booking" loading="lazy"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-xxlarge is-y-center">
                    <div class="header margin-bottom_none">
                        <div class="icon is-large is-background margin-bottom_xsmall">
                            <img src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68a9398ebf990d9aa40576fc_shopify_glyph_black.png" loading="lazy" alt="" class="image-5"/>
                        </div>
                        <h2>Sync shelves in seconds with Shelva</h2>
                        <p class="paragraph_large margin-bottom_none">Effortlessly link your Shopify online pricing and in-store pricing. Product updates, promotions, and inventory changes are instantly reflected on every shelf label—no manual edits, no mismatches, just accurate, up-to-date information at all times.</p>
                    </div>
                    <div class="image-ratio_1x1">
                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b0c24efa6118799a52ee7b_Untitled%20design%20(39).png" width="576" height="576" alt="Customer in store" loading="lazy"/>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Simple pricing for every shop</h2>
                </div>
                <ul role="list" class="list-4 w-list-unstyled">
                    <li class="card on-secondary">
                        <div class="card_body">
                            <div class="margin_bottom-auto">
                                <h4 class="heading_h3">Starter</h4>
                                <p class="paragraph-2">Connect up to 100 digital shelf labels. Perfect for small stores. Includes basic label design and instant updates.</p>
                            </div>
                            <div class="margin-top_large">
                                <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                    <p class="heading_h2 margin-bottom_none">$89</p>
                                    <p class="heading_h4 margin-bottom_none">/mo</p>
                                </div>
                                <p class="paragraph_large">First 100 labels</p>
                                <div class="margin-top_xsmall">
                                    <div class="button-group">
                                        <a href="https://apps.shopify.com/shelva-app" target="_blank" class="button w-button">Start</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="card on-secondary">
                        <div class="card_body">
                            <div class="margin_bottom-auto">
                                <h4 class="heading_h3">Growth</h4>
                                <p class="paragraph-3">Up to 200 shelf labels for expanding stores. Access advanced design, and priority support.</p>
                            </div>
                            <div class="margin-top_large">
                                <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                    <p class="heading_h2 margin-bottom_none">$149</p>
                                    <p class="heading_h4 margin-bottom_none">/mo</p>
                                </div>
                                <p class="paragraph_large">Up to 200 labels</p>
                                <div class="margin-top_xsmall">
                                    <div class="button-group">
                                        <a href="https://apps.shopify.com/shelva-app" target="_blank" class="button w-button">Grow</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="card on-secondary">
                        <div class="card_body">
                            <div class="margin_bottom-auto">
                                <h4 class="heading_h3">Enterprise</h4>
                                <p class="paragraph-4">Unlimited Shelva labels for expanding stores. personalized layout designs and priority support.</p>
                            </div>
                            <div class="margin-top_large">
                                <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                    <p class="heading_h4 margin-bottom_none">Contact sales</p>
                                </div>
                                <div class="margin-top_xsmall">
                                    <div class="button-group">
                                        <a href="mailto:contact@shelva.app?subject=Shelva%20Request" class="button w-button">Contact</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <div class="header max-width_large">
                    <h2 class="heading-2">Retail, reimagined for today</h2>
                    <p class="paragraph_large text-color_secondary">Bridge your online and in-store pricing. Update and manage electronic shelf labels directly from your Shopify admin—no extra tools or manual steps.</p>
                </div>
                <div class="w-layout-grid grid_3-col gap-xsmall">
                    <div class="card">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M9.24998 18.7103C6.60958 17.6271 4.75 15.0307 4.75 12C4.75 8.96938 6.60958 6.37304 9.24997 5.28979" stroke-width="1.5" stroke-linejoin="round" stroke="currentColor"></path>
                                    <path d="M14.75 5.28979C17.3904 6.37303 19.25 8.96938 19.25 12.0001C19.25 15.0307 17.3904 17.6271 14.75 18.7103" stroke-width="1.5" stroke-linejoin="round" stroke="currentColor"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Real-time price updates</h3>
                            <p class="margin-bottom_none">Shelf labels update instantly with every Shopify change. Eliminate mismatches and manual edits for accurate, up-to-date pricing and product data.</p>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M9.5 9C9.5 7.61929 10.6193 6.5 12 6.5C13.3807 6.5 14.5 7.61929 14.5 9C14.5 10.3807 13.3807 11.5 12 11.5C10.6193 11.5 9.5 10.3807 9.5 9Z" fill="currentColor"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Flexible label templates</h3>
                            <p class="margin-bottom_none">Design shelf labels with your branding, colors, and QR codes using our intuitive in-app editor—no design experience required.</p>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M4 12C8.41828 12 12 8.41828 12 4C12 8.41828 15.5817 12 20 12C15.5817 12 12 15.5817 12 20C12 15.5817 8.41828 12 4 12Z" stroke-width="1.5" stroke-linejoin="round" stroke="currentColor"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Centralized control</h3>
                            <p class="margin-bottom_none">Manage all shelf labels from one dashboard in Shopify. Scale across locations and keep every shelf in sync.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "how-it-works.html": {
        "title": "How It Works - Shelva Digital Shelf Labels",
        "description": "Learn how to set up Shelva digital shelf labels with your Shopify store. Step-by-step guide to installation, configuration, and management.",
        "active_nav": "HOW_IT_WORKS_ACTIVE",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">How Shelva Works</h1>
                    <p class="subheading">Get your digital shelf labels up and running in minutes with our simple setup process.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="header">
                    <h2 class="heading_h2">Getting Started</h2>
                </div>
                <div class="w-layout-grid grid_6-col">
                    <div class="card">
                        <div class="card_body">
                            <h1 class="heading-4">1.</h1>
                            <h3 class="heading_h4"><strong>Install the Shelva App</strong></h3>
                            <p class="paragraph_small margin-bottom_small">Install Shelva from the Shopify App Store. Take a moment to explore Shelva's easy-to-use features.</p>
                            <div class="image-ratio_16x9">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b117c5a42a200096c2ca67_6.png" width="1216" height="832" alt="App installation" loading="lazy"/>
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h1 class="heading-4">2.</h1>
                            <h3 class="heading_h4">Order Your Shelva Kit</h3>
                            <p class="paragraph_small margin-bottom_small">Choose and order the number of Shelva labels you need directly in the Shelva app. Labels currently available in Slim 2.9" or Spotlight 3.7" sizes.</p>
                            <div class="image-ratio_16x9">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c44bede78afd28e3958_3.png" width="1216" height="832" alt="Ordering process" loading="lazy"/>
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h1 class="heading-4">3.</h1>
                            <h3 class="heading_h4"><strong>Connect Base Station</strong></h3>
                            <p class="paragraph_small margin-bottom_small">Once received, plug in the base station with the included power and Ethernet cables, and it will automatically connect to your Shelva labels in minutes.</p>
                            <div class="image-ratio_16x9">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b1138b1fda442ca089fceb_AP%20Base%20Station%20(2).png" width="1216" height="832" alt="Base station setup" loading="lazy"/>
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h1 class="heading-4">4.</h1>
                            <h3 class="heading_h4"><strong>Customize Label Design</strong></h3>
                            <p class="paragraph_small margin-bottom_small">Use the built-in designer to add your logo, pick fonts and colors, and preview your digital shelf labels instantly.</p>
                            <div class="image-ratio_16x9">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b117c559d7f1762e78b05b_5.png" width="1216" height="832" alt="Label design" loading="lazy"/>
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h1 class="heading-4">5.</h1>
                            <h3 class="heading_h4">Publish to Shelves</h3>
                            <p class="paragraph_small margin-bottom_small">One click publishes your design, sending product names, prices, and more product info to every paired label.</p>
                            <div class="image-ratio_16x9">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b0c24efa6118799a52ee7b_Untitled%20design%20(39).png" width="1216" height="832" alt="Publishing labels" loading="lazy"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Why Choose Shelva?</h2>
                    <p class="paragraph_large">Built specifically for Shopify merchants with seamless integration and powerful features.</p>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Native Shopify Integration</h3>
                            <p class="margin-bottom_none">No CSV exports or separate portals. Everything works directly within your Shopify admin.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Real-time Sync</h3>
                            <p class="margin-bottom_none">Product changes, price updates, and inventory adjustments sync instantly to all your shelf labels.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Reliable & Secure</h3>
                            <p class="margin-bottom_none">Enterprise-grade security with 99.9% uptime and encrypted data transmission.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "pricing.html": {
        "title": "Pricing - Shelva Digital Shelf Labels",
        "description": "Transparent pricing for Shelva digital shelf labels. Choose the plan that fits your store size with no hidden fees or long-term commitments.",
        "active_nav": "PRICING_ACTIVE",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Simple, Transparent Pricing</h1>
                    <p class="subheading">Choose the plan that fits your store. No hidden fees, no long-term commitments.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_3-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <div class="margin_bottom-auto">
                                <h4 class="heading_h3">Starter</h4>
                                <p class="paragraph">Perfect for small stores getting started with digital shelf labels.</p>
                                <ul class="w-list-unstyled">
                                    <li>Up to 50 digital shelf labels</li>
                                    <li>Basic label design templates</li>
                                    <li>Real-time Shopify sync</li>
                                    <li>Email support</li>
                                    <li>Standard setup assistance</li>
                                </ul>
                            </div>
                            <div class="margin-top_large">
                                <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                    <p class="heading_h2 margin-bottom_none">$89</p>
                                    <p class="heading_h4 margin-bottom_none">/month</p>
                                </div>
                                <p class="paragraph_small text-color_secondary">Hardware sold separately</p>
                                <div class="margin-top_xsmall">
                                    <div class="button-group">
                                        <a href="https://apps.shopify.com/shelva-app" target="_blank" class="button w-button">Get Started</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card_body">
                            <div class="margin_bottom-auto">
                                <h4 class="heading_h3">Growth</h4>
                                <p class="paragraph">Ideal for expanding stores that need more labels and advanced features.</p>
                                <ul class="w-list-unstyled">
                                    <li>Up to 200 digital shelf labels</li>
                                    <li>Advanced label customization</li>
                                    <li>Priority sync (every 15 minutes)</li>
                                    <li>Phone & email support</li>
                                    <li>Dedicated account manager</li>
                                    <li>Multi-location support</li>
                                </ul>
                            </div>
                            <div class="margin-top_large">
                                <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                    <p class="heading_h2 margin-bottom_none">$149</p>
                                    <p class="heading_h4 margin-bottom_none">/month</p>
                                </div>
                                <p class="paragraph_small text-color_secondary">Hardware sold separately</p>
                                <div class="margin-top_xsmall">
                                    <div class="button-group">
                                        <a href="https://apps.shopify.com/shelva-app" target="_blank" class="button w-button">Get Started</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card_body">
                            <div class="margin_bottom-auto">
                                <h4 class="heading_h3">Enterprise</h4>
                                <p class="paragraph">For large retailers with complex needs and unlimited requirements.</p>
                                <ul class="w-list-unstyled">
                                    <li>Unlimited digital shelf labels</li>
                                    <li>Custom label designs</li>
                                    <li>Real-time sync (instant updates)</li>
                                    <li>24/7 priority support</li>
                                    <li>Dedicated success manager</li>
                                    <li>Custom integrations</li>
                                    <li>API access</li>
                                    <li>White-label options</li>
                                </ul>
                            </div>
                            <div class="margin-top_large">
                                <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                    <p class="heading_h4 margin-bottom_none">Contact Sales</p>
                                </div>
                                <p class="paragraph_small text-color_secondary">Custom pricing</p>
                                <div class="margin-top_xsmall">
                                    <div class="button-group">
                                        <a href="mailto:sales@shelva.app?subject=Enterprise%20Inquiry" class="button w-button">Contact Sales</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Hardware Pricing</h2>
                    <p class="paragraph_large">Refundable hardware deposits with 50% return value when you upgrade or cancel (within 12 months).</p>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Shelva Hub</h4>
                            <p class="paragraph_small">Base station for managing all your labels</p>
                            <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                <p class="heading_h3 margin-bottom_none">$299</p>
                                <p class="paragraph_small margin-bottom_none">one-time</p>
                            </div>
                            <p class="paragraph_small text-color_secondary">$149.50 refundable deposit</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Slim 2.9" Labels</h4>
                            <p class="paragraph_small">Perfect for most retail applications</p>
                            <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                <p class="heading_h3 margin-bottom_none">$29</p>
                                <p class="paragraph_small margin-bottom_none">each</p>
                            </div>
                            <p class="paragraph_small text-color_secondary">$14.50 refundable deposit</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Spotlight 3.7" Labels</h4>
                            <p class="paragraph_small">Larger format for detailed product info</p>
                            <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                <p class="heading_h3 margin-bottom_none">$39</p>
                                <p class="paragraph_small margin-bottom_none">each</p>
                            </div>
                            <p class="paragraph_small text-color_secondary">$19.50 refundable deposit</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Frequently Asked Questions</h2>
                </div>
                <div class="flex_vertical gap-medium">
                    <div class="divider">
                        <div class="heading_h4">Can I change my plan later?</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>Yes, you can upgrade or downgrade your plan at any time. Changes take effect on your next billing cycle, and we'll prorate any differences.</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h4">What happens to my hardware if I cancel?</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>You can return your hardware within 12 months for a 50% refund of the original purchase price, or keep it for future use if you decide to reactivate your account.</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h4">Is there a setup fee?</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>No setup fees. We provide free setup assistance and migration support to help you get started quickly.</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h4">Do you offer volume discounts?</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>Yes, we offer volume discounts for orders over 500 labels. Contact our sales team for custom pricing.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "order-labels.html": {
        "title": "Order Digital Shelf Labels - Shelva",
        "description": "Order Shelva digital shelf labels and hardware. Choose from Slim 2.9\" or Spotlight 3.7\" labels with flexible pricing and refundable deposits.",
        "active_nav": "",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Order Your Shelva Kit</h1>
                    <p class="subheading">Choose the perfect digital shelf labels for your store. All hardware comes with 50% refundable deposits.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_3-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Shelva Hub</h4>
                            <p class="paragraph">Base station that manages all your digital shelf labels</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b1138b1fda442ca089fceb_AP%20Base%20Station%20(2).png" alt="Shelva Hub" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled margin-bottom_medium">
                                <li>Ethernet connectivity</li>
                                <li>Manages up to 1000 labels</li>
                                <li>Secure encrypted communication</li>
                                <li>Easy setup and configuration</li>
                            </ul>
                            <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                <p class="heading_h2 margin-bottom_none">$299</p>
                                <p class="paragraph_small margin-bottom_none">one-time</p>
                            </div>
                            <p class="paragraph_small text-color_secondary">$149.50 refundable deposit</p>
                            <div class="margin-top_xsmall">
                                <div class="button-group">
                                    <a href="https://apps.shopify.com/shelva-app" class="button w-button">Order Now</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Slim 2.9" Labels</h4>
                            <p class="paragraph">Perfect for most retail applications with compact design</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c44bede78afd28e3958_3.png" alt="Slim Labels" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled margin-bottom_medium">
                                <li>2.9" e-ink display</li>
                                <li>Battery life: 5+ years</li>
                                <li>Weather resistant</li>
                                <li>Easy mounting system</li>
                            </ul>
                            <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                <p class="heading_h2 margin-bottom_none">$29</p>
                                <p class="paragraph_small margin-bottom_none">each</p>
                            </div>
                            <p class="paragraph_small text-color_secondary">$14.50 refundable deposit</p>
                            <div class="margin-top_xsmall">
                                <div class="button-group">
                                    <a href="https://apps.shopify.com/shelva-app" class="button w-button">Order Now</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Spotlight 3.7" Labels</h4>
                            <p class="paragraph">Larger format for detailed product information and promotions</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c435113c826aa536b89_2.png" alt="Spotlight Labels" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled margin-bottom_medium">
                                <li>3.7" e-ink display</li>
                                <li>Battery life: 5+ years</li>
                                <li>High contrast display</li>
                                <li>QR code support</li>
                            </ul>
                            <div class="w-layout-hflex flex_horizontal is-y-baseline">
                                <p class="heading_h2 margin-bottom_none">$39</p>
                                <p class="paragraph_small margin-bottom_none">each</p>
                            </div>
                            <p class="paragraph_small text-color_secondary">$19.50 refundable deposit</p>
                            <div class="margin-top_xsmall">
                                <div class="button-group">
                                    <a href="https://apps.shopify.com/shelva-app" class="button w-button">Order Now</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Volume Discounts</h2>
                    <p class="paragraph_large">Save more when you order in bulk</p>
                </div>
                <div class="w-layout-grid grid_4-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">50+ Labels</h4>
                            <p class="paragraph_small">5% discount</p>
                            <p class="heading_h3">$27.55 each</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">100+ Labels</h4>
                            <p class="paragraph_small">10% discount</p>
                            <p class="heading_h3">$26.10 each</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">250+ Labels</h4>
                            <p class="paragraph_small">15% discount</p>
                            <p class="heading_h3">$24.65 each</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">500+ Labels</h4>
                            <p class="paragraph_small">20% discount</p>
                            <p class="heading_h3">$23.20 each</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "design.html": {
        "title": "Design Your Digital Shelf Labels - Shelva",
        "description": "Customize your digital shelf labels with Shelva's design tools. Add logos, choose fonts, colors, and layouts to match your brand.",
        "active_nav": "",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Design Your Labels</h1>
                    <p class="subheading">Create custom digital shelf labels that match your brand. No design experience required.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-xxlarge is-y-center">
                    <div class="header margin-bottom_none">
                        <h2 class="heading_h2">Make it yours</h2>
                        <p class="paragraph_large margin-bottom_none">Design shelf labels that reflect your brand with our intuitive editor. Choose from templates or start from scratch.</p>
                        <div class="margin-top_medium">
                            <div class="button-group">
                                <a href="https://apps.shopify.com/shelva-app" class="button w-button">Start Designing</a>
                            </div>
                        </div>
                    </div>
                    <div class="image-ratio_1x1">
                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b117c559d7f1762e78b05b_5.png" alt="Label design interface" loading="lazy"/>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Design Features</h2>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Brand Customization</h3>
                            <p class="margin-bottom_none">Upload your logo, choose brand colors, and select fonts that match your store's identity.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Live Preview</h3>
                            <p class="margin-bottom_none">See your changes instantly with our live preview feature. No guessing how your labels will look.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M4 12C8.41828 12 12 8.41828 12 4C12 8.41828 15.5817 12 20 12C15.5817 12 12 15.5817 12 20C12 15.5817 8.41828 12 4 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Template Library</h3>
                            <p class="margin-bottom_none">Start with professional templates designed for different retail categories and customize from there.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Label Size Options</h2>
                    <p class="paragraph_large">Choose the perfect size for your products and store layout</p>
                </div>
                <div class="w-layout-grid grid_2-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Slim 2.9" Labels</h4>
                            <p class="paragraph">Perfect for most retail applications</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c44bede78afd28e3958_3.png" alt="Slim labels" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled">
                                <li>Compact design</li>
                                <li>Price and product name</li>
                                <li>Basic product info</li>
                                <li>Perfect for tight spaces</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Spotlight 3.7" Labels</h4>
                            <p class="paragraph">Larger format for detailed information</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c435113c826aa536b89_2.png" alt="Spotlight labels" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled">
                                <li>More display space</li>
                                <li>Detailed descriptions</li>
                                <li>QR codes</li>
                                <li>Promotional content</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "features.html": {
        "title": "Features - Shelva Digital Shelf Labels",
        "description": "Discover all the powerful features of Shelva digital shelf labels. Real-time sync, bulk management, custom designs, and more.",
        "active_nav": "FEATURES_ACTIVE",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Powerful Features</h1>
                    <p class="subheading">Everything you need to manage your digital shelf labels efficiently and effectively.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-xxlarge is-y-center">
                    <div class="header margin-bottom_none">
                        <h2 class="heading_h2">Real-time Synchronization</h2>
                        <p class="paragraph_large margin-bottom_none">Your shelf labels update instantly when you make changes in Shopify. No manual work, no delays, no errors.</p>
                        <ul class="w-list-unstyled margin-top_medium">
                            <li>Price changes sync in seconds</li>
                            <li>Inventory updates automatically</li>
                            <li>Product information stays current</li>
                            <li>Promotions display instantly</li>
                        </ul>
                    </div>
                    <div class="image-ratio_1x1">
                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b0c24efa6118799a52ee7b_Untitled%20design%20(39).png" alt="Real-time sync" loading="lazy"/>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Advanced Management</h2>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Bulk Operations</h3>
                            <p class="margin-bottom_none">Update hundreds of labels at once with bulk operations. Change prices, apply promotions, or update product information across your entire store.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Low Battery Alerts</h3>
                            <p class="margin-bottom_none">Get notified when labels are running low on battery. Plan replacements proactively to avoid any downtime.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M4 12C8.41828 12 12 8.41828 12 4C12 8.41828 15.5817 12 20 12C15.5817 12 12 15.5817 12 20C12 15.5817 8.41828 12 4 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Flash LED Locator</h3>
                            <p class="margin-bottom_none">Find specific labels instantly with the flash LED feature. Perfect for large stores with hundreds of labels.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Smart Automation</h2>
                </div>
                <div class="w-layout-grid grid_2-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Auto-Sync Scheduling</h4>
                            <p class="paragraph">Set up automatic synchronization schedules that work with your business hours and update patterns.</p>
                            <ul class="w-list-unstyled">
                                <li>Daily price updates</li>
                                <li>Weekly inventory sync</li>
                                <li>Promotional campaigns</li>
                                <li>Seasonal adjustments</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Multi-Store Support</h4>
                            <p class="paragraph">Manage multiple store locations from a single dashboard. Perfect for retail chains and franchises.</p>
                            <ul class="w-list-unstyled">
                                <li>Centralized control</li>
                                <li>Location-specific pricing</li>
                                <li>Regional promotions</li>
                                <li>Unified reporting</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "about.html": {
        "title": "About Shelva - Digital Shelf Label Solutions",
        "description": "Learn about Shelva's mission to modernize retail with digital shelf labels. Meet our team and discover our vision for the future of retail.",
        "active_nav": "ABOUT_ACTIVE",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">About Shelva</h1>
                    <p class="subheading">We're on a mission to modernize retail with smart, connected digital shelf labels.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-xxlarge is-y-center">
                    <div class="header margin-bottom_none">
                        <h2 class="heading_h2">Our Story</h2>
                        <p class="paragraph_large margin-bottom_none">Shelva was born from a simple observation: retail stores were still using paper price tags in the digital age. We saw an opportunity to bridge the gap between online and in-store experiences.</p>
                        <p class="paragraph_large margin-top_medium">Founded by Ethan Giller, a retail technology veteran, Shelva combines deep industry knowledge with cutting-edge technology to create solutions that actually work for merchants.</p>
                    </div>
                    <div class="image-ratio_1x1">
                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68a935e1326d9198359766a5_Shelva%20logo%20-%20ethans%20pick-01-01.png" alt="Shelva team" loading="lazy"/>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Our Mission</h2>
                    <p class="paragraph_large">To empower retailers with technology that simplifies operations and enhances customer experiences.</p>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Simplify Operations</h3>
                            <p class="margin-bottom_none">We believe technology should make retail operations simpler, not more complex. Our solutions are designed to be intuitive and easy to use.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Enhance Experiences</h3>
                            <p class="margin-bottom_none">Every feature we build is designed to improve the experience for both merchants and their customers.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M4 12C8.41828 12 12 8.41828 12 4C12 8.41828 15.5817 12 20 12C15.5817 12 12 15.5817 12 20C12 15.5817 8.41828 12 4 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Drive Innovation</h3>
                            <p class="margin-bottom_none">We're constantly pushing the boundaries of what's possible in retail technology, always looking for the next breakthrough.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Meet the Team</h2>
                </div>
                <div class="w-layout-grid grid_2-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Ethan Giller</h4>
                            <p class="paragraph_small text-color_secondary">Founder & CEO</p>
                            <p class="paragraph">Ethan brings over 10 years of experience in retail technology and e-commerce. Previously led product development at several successful retail tech startups, focusing on the intersection of online and offline commerce.</p>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Our Vision</h4>
                            <p class="paragraph">We envision a future where every retail store is as connected and efficient as the best online experiences. Where merchants can focus on what they do best—serving customers—while technology handles the complexity behind the scenes.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "contact.html": {
        "title": "Contact Shelva - Get Support & Sales Information",
        "description": "Get in touch with Shelva for sales inquiries, technical support, or general questions about our digital shelf label solutions.",
        "active_nav": "CONTACT_ACTIVE",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Get in Touch</h1>
                    <p class="subheading">We're here to help you succeed with digital shelf labels. Reach out for sales, support, or any questions.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-xxlarge">
                    <div class="header margin-bottom_none">
                        <h2 class="heading_h2">Contact Information</h2>
                        <p class="paragraph_large margin-bottom_none">Choose the best way to reach us based on your needs.</p>
                    </div>
                    <div class="w-layout-grid grid_2-col gap-medium">
                        <div class="card">
                            <div class="card_body">
                                <div class="icon margin-bottom_xsmall">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                        <path d="M5.25 6.75H18.75V17.25H5.25V6.75Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"></path>
                                        <path d="M5.25 6.75L12 12L18.75 6.75" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"></path>
                                    </svg>
                                </div>
                                <h4 class="heading_h4">Sales Inquiries</h4>
                                <p class="paragraph_small">For pricing, demos, and enterprise solutions</p>
                                <a href="mailto:sales@shelva.app" class="text-link">sales@shelva.app</a>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card_body">
                                <div class="icon margin-bottom_xsmall">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                        <path d="M12.5 18.25C16.2279 18.25 19.25 15.2279 19.25 11.5C19.25 7.77208 16.2279 4.75 12.5 4.75C8.77208 4.75 5.75 7.77208 5.75 11.5C5.75 12.6007 6.01345 13.6398 6.48072 14.5578L5 19L9.71819 17.6519C10.5664 18.0361 11.5082 18.25 12.5 18.25Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"></path>
                                    </svg>
                                </div>
                                <h4 class="heading_h4">Technical Support</h4>
                                <p class="paragraph_small">Setup help and troubleshooting</p>
                                <a href="mailto:support@shelva.app" class="text-link">support@shelva.app</a>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card_body">
                                <div class="icon margin-bottom_xsmall">
                                    <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                        <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                    </svg>
                                </div>
                                <h4 class="heading_h4">General Questions</h4>
                                <p class="paragraph_small">Partnerships and general inquiries</p>
                                <a href="mailto:contact@shelva.app" class="text-link">contact@shelva.app</a>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card_body">
                                <div class="icon margin-bottom_xsmall">
                                    <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                        <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                    </svg>
                                </div>
                                <h4 class="heading_h4">Live Chat</h4>
                                <p class="paragraph_small">Weekdays, 8am–5pm EST</p>
                                <p class="paragraph_small">Available in the Shelva app</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Response Times</h2>
                    <p class="paragraph_large">We're committed to getting back to you quickly</p>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Sales Inquiries</h4>
                            <p class="paragraph_small">Response within 2 hours during business hours</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Technical Support</h4>
                            <p class="paragraph_small">Response within 4 hours, 24/7 for critical issues</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">General Questions</h4>
                            <p class="paragraph_small">Response within 24 hours</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "technology.html": {
        "title": "Technology - Shelva Digital Shelf Labels",
        "description": "Learn about Shelva's technical architecture, security, and reliability. Built for enterprise-grade performance with Shopify integration.",
        "active_nav": "",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Built for Reliability</h1>
                    <p class="subheading">Enterprise-grade technology that powers your digital shelf labels with 99.9% uptime and bank-level security.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="w-layout-grid grid_2-col tablet-1-col gap-xxlarge is-y-center">
                    <div class="header margin-bottom_none">
                        <h2 class="heading_h2">Architecture Overview</h2>
                        <p class="paragraph_large margin-bottom_none">Shelva's architecture is designed for scalability, security, and reliability. Our system handles everything from data synchronization to device management.</p>
                        <ul class="w-list-unstyled margin-top_medium">
                            <li>Cloud-based infrastructure</li>
                            <li>Real-time data synchronization</li>
                            <li>Encrypted communication</li>
                            <li>Automatic failover</li>
                        </ul>
                    </div>
                    <div class="image-ratio_1x1">
                        <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b1138b1fda442ca089fceb_AP%20Base%20Station%20(2).png" alt="System architecture" loading="lazy"/>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Security & Compliance</h2>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M9 12L11 14L15 10M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Data Encryption</h3>
                            <p class="margin-bottom_none">All data transmission is encrypted using industry-standard TLS 1.3 encryption. Your product information and pricing data is protected at every step.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">Shopify Integration</h3>
                            <p class="margin-bottom_none">Secure API integration with Shopify using OAuth 2.0. Your data never leaves Shopify's secure environment without proper authorization.</p>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <div class="icon margin-bottom_xsmall">
                                <svg width="100%" height="100%" viewBox="0 0 24 24" fill="none">
                                    <path d="M4 12C8.41828 12 12 8.41828 12 4C12 8.41828 15.5817 12 20 12C15.5817 12 12 15.5817 12 20C12 15.5817 8.41828 12 4 12Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"></path>
                                </svg>
                            </div>
                            <h3 class="heading_h4">SOC 2 Compliance</h3>
                            <p class="margin-bottom_none">We maintain SOC 2 Type II compliance, ensuring the highest standards of security, availability, and confidentiality for your data.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Performance & Reliability</h2>
                </div>
                <div class="w-layout-grid grid_2-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">99.9% Uptime SLA</h4>
                            <p class="paragraph">Our infrastructure is designed for maximum reliability with automatic failover and redundant systems.</p>
                            <ul class="w-list-unstyled">
                                <li>Multi-region deployment</li>
                                <li>Automatic load balancing</li>
                                <li>Real-time monitoring</li>
                                <li>Instant failover</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Real-time Sync</h4>
                            <p class="paragraph">Changes in Shopify are reflected on your shelf labels within seconds, not minutes or hours.</p>
                            <ul class="w-list-unstyled">
                                <li>Webhook-based updates</li>
                                <li>MQTT communication</li>
                                <li>Optimized data transfer</li>
                                <li>Smart caching</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "docs/shelva-app/get-started.html": {
        "title": "Get Started with Shelva - Setup Guide",
        "description": "Complete setup guide for Shelva digital shelf labels. Learn how to install, configure, and manage your digital shelf label system.",
        "active_nav": "",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Get Started with Shelva</h1>
                    <p class="subheading">Complete setup guide to get your digital shelf labels up and running in minutes.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="header">
                    <h2 class="heading_h2">Prerequisites</h2>
                    <p class="paragraph_large">Before you begin, make sure you have the following:</p>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h4">Shopify Store</h4>
                            <p class="paragraph_small">An active Shopify store with admin access</p>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h4">Internet Connection</h4>
                            <p class="paragraph_small">Stable internet connection for your base station</p>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h4">Shelva Hardware</h4>
                            <p class="paragraph_small">Shelva Hub and digital shelf labels</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header">
                    <h2 class="heading_h2">Step-by-Step Setup</h2>
                </div>
                <div class="flex_vertical gap-large">
                    <div class="divider">
                        <div class="heading_h3">Step 1: Install the Shelva App</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>1. Go to the <a href="https://apps.shopify.com/shelva-app" target="_blank">Shopify App Store</a></p>
                            <p>2. Click "Add app" to install Shelva</p>
                            <p>3. Grant the necessary permissions when prompted</p>
                            <p>4. Complete the initial setup wizard</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h3">Step 2: Set Up Your Base Station</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>1. Connect the Shelva Hub to your router using the included Ethernet cable</p>
                            <p>2. Plug in the power adapter</p>
                            <p>3. Wait for the status LED to turn green (indicates successful connection)</p>
                            <p>4. The app will automatically detect your base station</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h3">Step 3: Pair Your Labels</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>1. Open the Shelva app in your Shopify admin</p>
                            <p>2. Go to the "Labels" section</p>
                            <p>3. Click "Add New Labels"</p>
                            <p>4. Follow the on-screen instructions to pair each label</p>
                            <p>5. Assign labels to specific products or categories</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h3">Step 4: Design Your Labels</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>1. Navigate to the "Design" section in the app</p>
                            <p>2. Choose a template or start from scratch</p>
                            <p>3. Customize fonts, colors, and layout</p>
                            <p>4. Add your logo and branding elements</p>
                            <p>5. Preview your design before applying</p>
                        </div>
                    </div>
                    <div class="divider">
                        <div class="heading_h3">Step 5: Publish and Test</div>
                        <div class="rich-text paragraph_large w-richtext">
                            <p>1. Click "Publish to Labels" to send your design to all labels</p>
                            <p>2. Verify that labels are displaying correctly</p>
                            <p>3. Test price changes in Shopify to ensure real-time sync</p>
                            <p>4. Set up automatic sync schedules if needed</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Troubleshooting</h2>
                </div>
                <div class="w-layout-grid grid_2-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h4">Base Station Not Connecting</h4>
                            <ul class="w-list-unstyled">
                                <li>Check Ethernet cable connection</li>
                                <li>Verify internet connectivity</li>
                                <li>Restart the base station</li>
                                <li>Contact support if issues persist</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h4">Labels Not Updating</h4>
                            <ul class="w-list-unstyled">
                                <li>Check label battery levels</li>
                                <li>Verify label pairing</li>
                                <li>Test sync manually</li>
                                <li>Check for app updates</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    
    "retailers.html": {
        "title": "For Retailers - Shelva Digital Shelf Labels",
        "description": "Discover how different retail businesses use Shelva digital shelf labels to improve operations, reduce costs, and enhance customer experience.",
        "active_nav": "",
        "content": """
        <header class="section is-accent-primary">
            <div class="container is-small">
                <div class="header is-align-center">
                    <h1 class="heading_h1">Perfect for Every Retail Business</h1>
                    <p class="subheading">See how different types of retailers use Shelva to streamline operations and improve customer experience.</p>
                </div>
            </div>
        </header>
        
        <section class="section">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Retail Categories</h2>
                </div>
                <div class="w-layout-grid grid_3-col gap-large">
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Fashion & Apparel</h4>
                            <p class="paragraph">Perfect for clothing stores with frequent price changes and seasonal promotions.</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c44bede78afd28e3958_3.png" alt="Fashion retail" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled">
                                <li>Seasonal price updates</li>
                                <li>Size and color variations</li>
                                <li>Sale promotions</li>
                                <li>Inventory management</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Electronics</h4>
                            <p class="paragraph">Ideal for tech stores with complex product specifications and frequent price changes.</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68ae0c435113c826aa536b89_2.png" alt="Electronics retail" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled">
                                <li>Detailed specifications</li>
                                <li>Model comparisons</li>
                                <li>Warranty information</li>
                                <li>Technical details</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card_body">
                            <h4 class="heading_h3">Home & Garden</h4>
                            <p class="paragraph">Great for home improvement stores with diverse product categories and seasonal items.</p>
                            <div class="image-ratio_3x2 margin-bottom_medium">
                                <img class="image_cover" src="https://cdn.prod.website-files.com/68a8e7ca6773a5df8483416a/68b0c24efa6118799a52ee7b_Untitled%20design%20(39).png" alt="Home & garden retail" loading="lazy"/>
                            </div>
                            <ul class="w-list-unstyled">
                                <li>Seasonal pricing</li>
                                <li>Product dimensions</li>
                                <li>Care instructions</li>
                                <li>Compatibility info</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section is-secondary">
            <div class="container">
                <div class="header is-align-center">
                    <h2 class="heading_h2">Benefits by Business Size</h2>
                </div>
                <div class="w-layout-grid grid_3-col gap-medium">
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Small Stores (1-2 locations)</h4>
                            <ul class="w-list-unstyled">
                                <li>Reduce manual price updates by 90%</li>
                                <li>Eliminate pricing errors</li>
                                <li>Focus on customer service</li>
                                <li>Quick setup and deployment</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Medium Chains (3-10 locations)</h4>
                            <ul class="w-list-unstyled">
                                <li>Centralized price management</li>
                                <li>Consistent branding across stores</li>
                                <li>Regional pricing strategies</li>
                                <li>Unified inventory tracking</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card on-secondary">
                        <div class="card_body">
                            <h4 class="heading_h4">Large Retailers (10+ locations)</h4>
                            <ul class="w-list-unstyled">
                                <li>Enterprise-grade scalability</li>
                                <li>Custom integrations</li>
                                <li>Advanced analytics</li>
                                <li>Dedicated support</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    }
}

def generate_page(filename, page_data):
    """Generate a single page from template and data"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace template variables
    content = template
    content = content.replace('{{PAGE_TITLE}}', page_data['title'])
    content = content.replace('{{PAGE_DESCRIPTION}}', page_data['description'])
    content = content.replace('{{PAGE_CONTENT}}', page_data['content'])
    
    # Set active navigation
    for nav_key in ['HOME_ACTIVE', 'HOW_IT_WORKS_ACTIVE', 'PRICING_ACTIVE', 'FEATURES_ACTIVE', 'ABOUT_ACTIVE', 'CONTACT_ACTIVE']:
        if nav_key == page_data.get('active_nav', ''):
            content = content.replace(f'{{{{{nav_key}}}}}', 'w--current')
        else:
            content = content.replace(f'{{{{{nav_key}}}}}', '')
    
    # Write the file
    output_path = f"site/{filename}"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated: {output_path}")

def main():
    """Generate all pages"""
    print("Generating Shelva marketing pages...")
    
    # Create directories if needed
    os.makedirs("site/docs/shelva-app", exist_ok=True)
    
    # Generate each page
    for filename, page_data in PAGES.items():
        generate_page(filename, page_data)
    
    print(f"Generated {len(PAGES)} pages successfully!")
    print("\nFiles created:")
    for filename in PAGES.keys():
        print(f"  - site/{filename}")

if __name__ == "__main__":
    main()
