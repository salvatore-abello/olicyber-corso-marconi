
# Example 1 - Reflected

https://example.com/status?message=<script>alert()</script>

# Example 2 - DOM based

```js
var search = document.getElementById('search').value;
var results = document.getElementById('results');
results.innerHTML = 'You searched for: ' + search;
```