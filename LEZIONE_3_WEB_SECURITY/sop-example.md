
# Example 1 - Different origin

```js
// In http://attacker.com
fetch("http://example.com/currentUser") // Errore!
```

# Example 2 - Same origin

```js
// In http://example.com/
fetch("http://example.com/currentUser") // Apposto
```

