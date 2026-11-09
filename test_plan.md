# Test Plan: automationexercise.com

## Scope

Functional UI and API testing of [automationexercise.com](https://www.automationexercise.com), a practice e-commerce site. UI cases follow the site's [test case list](https://www.automationexercise.com/test_cases). API cases come from the site's [API list](https://www.automationexercise.com/api_list).

## Approach

- **UI:** Playwright with pytest, using page objects (`ui_tests/`)
- **API:** requests with pytest (`api_tests/`)
- **Data:** generated with Faker, with a UUID in each signup email so accounts never collide
- **CI:** GitHub Actions runs both suites on every push
- **Out of scope:** performance, security, cross-browser (Chromium only), mobile

## Status key

Done = automated and passing | Skipped = automated, disabled | Not started

## UI test cases

| # | Test case | Status | Test file | Notes |
|---|-----------|--------|-----------|-------|
| 1 | Register user | Done | test_auth.py | Includes verify "Logged in as" and delete account |
| 2 | Login with correct credentials | Done | test_auth.py | Uses `registered_user` fixture |
| 3 | Login with incorrect credentials | Done | test_auth.py | |
| 4 | Logout user | Not started | | `click_logout` already exists in `AuthPage` |
| 5 | Register with existing email | Not started | | |
| 6 | Contact us form | Not started | | File upload and dialog handling |
| 7 | Verify test cases page | Not started | | |
| 8 | Verify all products and product detail | Not started | | |
| 9 | Search product | Done | test_products.py | Searches "Blue Top", checks every result name |
| 10 | Verify subscription on home page | Not started | | |
| 11 | Verify subscription on cart page | Not started | | |
| 12 | Add products to cart | Not started | | |
| 13 | Verify product quantity in cart | Not started | | |
| 14 | Place order: register while checkout | Not started | | |
| 15 | Place order: register before checkout | Not started | | |
| 16 | Place order: login before checkout | Not started | | |
| 17 | Remove products from cart | Not started | | |
| 18 | View category products | Not started | | |
| 19 | View and cart brand products | Not started | | |
| 20 | Search products and verify cart after login | Not started | | |
| 21 | Add review on product | Not started | | |
| 22 | Add to cart from recommended items | Not started | | |
| 23 | Verify address details in checkout | Not started | | |
| 24 | Download invoice after purchase | Skipped | test_products.py | WIP: add-to-cart locator times out |
| 25 | Scroll up using arrow button | Not started | | |
| 26 | Scroll up without arrow button | Not started | | |

Additional UI checks (not numbered on the site):

| Check | Status | Test file |
|-------|--------|-----------|
| Home page is visible | Done | test_home.py |
| "New User Signup!" is visible on the login page | Done | test_auth.py |
| Signup advances to "Enter Account Information" | Done | test_auth.py |

## API test cases

| # | Endpoint | Case | Status | Expected |
|---|----------|------|--------|----------|
| 1 | GET /api/productsList | All products | Done | responseCode 200, non-empty list |
| 2 | POST /api/productsList | Unsupported method | Done | responseCode 405 |
| 5 | POST /api/searchProduct | With valid term | Done | responseCode 200, results match term |
| 6 | POST /api/searchProduct | Without parameter | Done | responseCode 400 |
| 7 | POST /api/verifyLogin | Valid credentials | Done | responseCode 200 (user created and deleted by fixture) |
| 9 | POST /api/verifyLogin | Invalid credentials | Done | responseCode 404 |
| 3 | GET /api/brandsList | All brands | Not started | |
| 4 | PUT /api/brandsList | Unsupported method | Not started | |
| 8 | POST /api/verifyLogin | Without email | Not started | |
| 10 | DELETE /api/verifyLogin | Unsupported method | Not started | |
| 11 | POST /api/createAccount | Create account | Fixture only | Used in `api_user`, no dedicated test |
| 12 | DELETE /api/deleteAccount | Delete account | Fixture only | Used as cleanup in `api_user` |
| 13 | PUT /api/updateAccount | Update account | Not started | |
| 14 | GET /api/getUserDetailByEmail | Get user details | Not started | |

## Known issues and risks

- **Skipped:** checkout and invoice test (case 24), pending a fix to the add-to-cart locator
- **Flakiness:** ad overlays (`#google_vignette`) can block clicks intermittently
- **External dependency:** the site is public and shared, so slowness or downtime can fail CI for reasons unrelated to the code
- **Test data:** failed UI tests may leave accounts behind. API fixtures clean up after themselves.

## Next steps

1. Fix and re-enable the checkout test
2. Add logout, register with existing email, and cart cases
3. Create the UI `registered_user` through `/api/createAccount` to speed up login tests
4. Add the remaining API cases (brands, verify login without email, update account, get user by email)
