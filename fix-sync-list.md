# Sync Errors Fix List

## YAML Parsing Errors

### 1. Bitcoin Lille (cs.yml)
- **File**: `resources/projects/bitcoin-lile/cs.yml`
- **Error**: Unexpected end of the stream within a double quoted scalar at line 2:1
- **Issue**: Description field has unclosed quotes
- **Fix**: Close the quotes in the description field

### 2. Bitcoin Saigon (project.yml)
- **File**: `resources/projects/bitcoin-saigon/cs.yml`
- **Error**: TypeError: p.contributor_names.entries is not a function
- **Issue**: contributor_names field has incorrect format
- **Fix**: Ensure contributor_names is properly formatted as an array

### 3. BoltFun (fa.yml)
- **File**: `resources/projects/boltfun/cs.yml`
- **Error**: A line break is expected at line 1:15
- **Issue**: Invalid YAML syntax with "|۲"
- **Fix**: Correct the multiline string syntax

### 4. Chaincode (fa.yml)
- **File**: `resources/projects/chaincode/cs.yml`
- **Error**: A line break is expected at line 1:15
- **Issue**: Invalid YAML syntax with "|۲"
- **Fix**: Correct the multiline string syntax

### 5. Plebs Together Strong (cs.yml)
- **File**: `resources/projects/plebs-together-strong/cs.yml`
- **Error**: Unexpected end of the stream within a double quoted scalar at line 2:1
- **Issue**: Description field has unclosed quotes
- **Fix**: Close the quotes in the description field

### 6. Bitcoin and the Trust Problem (fa.yml)
- **File**: `resources/books/bitcoin-and-the-trust-problem/book.yml`
- **Error**: Unexpected end of the stream within a double quoted scalar at line 7:1
- **Issue**: Multiline description field not properly closed
- **Fix**: Properly format the multiline description

### 7. Bitcoin The Ultimate Collateral (zh-Hans.yml)
- **File**: `resources/books/bitcoin-the-ultimate-collateral/book.yml`
- **Error**: Unexpected end of the stream within a double quoted scalar at line 15:1
- **Issue**: Multiline description field not properly closed
- **Fix**: Properly format the multiline description

### 8. Fossil Future (sv.yml)
- **File**: `resources/books/fossil-future/book.yml`
- **Error**: Bad indentation of a mapping entry at line 6:6
- **Issue**: Incorrect indentation in description field
- **Fix**: Fix the indentation of the description content

### 9. Monetary Regimes and Inflation (fa.yml)
- **File**: `resources/books/monetary-regimes-and-inflation-history-economic-and-political-relationships-second-edition/book.yml`
- **Error**: Unexpected end of the stream within a double quoted scalar at line 7:1
- **Issue**: Empty or improperly formatted description field
- **Fix**: Add proper content to the description field

## Database Errors

### 10. Bitsacco Project
- **File**: `resources/projects/bitsacco/cs.yml`
- **Error**: PostgresError: null value in column "id" violates not-null constraint
- **Issue**: Missing required ID field
- **Fix**: Add a valid UUID for the project ID

### 11. BTC101 Course (th.md)
- **File**: `courses/btc101/course.yml`
- **Error**: PostgresError: invalid input syntax for type uuid: ""
- **Issue**: Empty or invalid UUID value
- **Fix**: Provide a valid UUID or remove the empty field

### 12. Blitz Wallet Tutorial (es.md)
- **File**: `tutorials/wallet/blitz-wallet/cs.md`
- **Error**: PostgresError: null value in column "title" violates not-null constraint
- **Issue**: Missing title field in Spanish localization
- **Fix**: Add the required title field

### 13. Bitcoin Flea Market Event
- **File**: `events/bitcoin-flea-market-summer-2025`
- **Error**: PostgresError: invalid input value for enum event_type: "market"
- **Issue**: "market" is not a valid event type
- **Fix**: Use a valid event_type value from the allowed enum values

## Summary

Total errors: 13
- YAML parsing errors: 9
- Database constraint errors: 4

### Priority Fixes
1. Fix all YAML syntax errors (unclosed quotes, invalid multiline syntax, indentation)
2. Add missing required fields (IDs, titles)
3. Use valid enum values for event types
4. Ensure all UUID fields contain valid UUIDs