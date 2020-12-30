# Address finder

Given string of addresses this project will extract street name and house number out of those.

### Example 

```buildoutcfg
1. simple case:
"Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
"Musterstrasse 45" -> {"street": "Musterstrasse", "housenumber": "45"}
"Blaufeldweg 123B" -> {"street": "Blaufeldweg", "housenumber": "123B"}

2. Complex case:
"4, rue de la revolution" -> {"street": "rue de la revolution", "housenumber": "4"}
"200 Broadway Av" -> {"street": "Broadway Av", "housenumber": "200"}
"Calle Aduana, 29" -> {"street": "Calle Aduana", "housenumber": "29"}
"Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}

```