import asyncio
from playwright.async_api import async_playwright
import os

async def verify_carousel():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        
        # Navigate to homepage
        await page.goto("http://localhost:8000", wait_until="networkidle")
        print(f"Page title: {await page.title()}")
        
        # Take full page screenshot
        await page.screenshot(path="fullpage.png", full_page=True)
        print("Saved fullpage.png")
        
        # Check if registered companies section exists
        reg_section = await page.query_selector(".registered-section")
        if reg_section:
            print("[OK] Registered companies section found")
            
            # Check carousel container
            carousel = await page.query_selector("#carousel-3d-container")
            if carousel:
                print("[OK] 3D carousel container found")
                
                # Check carousel items
                items = await page.query_selector_all(".carousel-3d-item")
                print(f"[OK] Found {len(items)} carousel items")
                
                # Check first item's transform style
                if items:
                    first_item = items[0]
                    transform = await first_item.get_attribute("style")
                    print(f"[OK] First item style: {transform}")
                
                # Check dots
                dots = await page.query_selector_all(".reg-dot")
                print(f"[OK] Found {len(dots)} navigation dots")
                
                # Check nav buttons
                prev_btn = await page.query_selector(".reg-prev")
                next_btn = await page.query_selector(".reg-next")
                if prev_btn and next_btn:
                    print("[OK] Navigation buttons found")
                
                # Screenshot just the carousel section
                await reg_section.screenshot(path="carousel_section.png")
                print("Saved carousel_section.png")
                
                # Test clicking next button
                if next_btn:
                    await next_btn.click()
                    await asyncio.sleep(1)
                    await reg_section.screenshot(path="carousel_after_click.png")
                    print("Saved carousel_after_click.png (after clicking next)")
                    
                    # Verify items changed
                    items_after = await page.query_selector_all(".carousel-3d-item")
                    if items_after:
                        first_item_after = items_after[0]
                        transform_after = await first_item_after.get_attribute("style")
                        print(f"[OK] First item style after click: {transform_after}")
            else:
                print("[FAIL] 3D carousel container NOT found")
        else:
            print("[FAIL] Registered companies section NOT found")
            
            # Debug: check what sections exist
            sections = await page.query_selector_all("section")
            print(f"\nDebug: Found {len(sections)} sections on page:")
            for i, section in enumerate(sections):
                classes = await section.get_attribute("class")
                print(f"  {i+1}. {classes}")
        
        await browser.close()

asyncio.run(verify_carousel())
