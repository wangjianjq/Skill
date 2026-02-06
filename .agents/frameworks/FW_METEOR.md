---
tags: ["backend", "node", "realtime"]
---
# Framework: Meteor

## Schema: Framework Specification

- framework: Meteor
- category: web
- language: JavaScript/TypeScript
- latest_supported_version: 3.x
- rendering_engine: Blaze/React/Vue
- state_management: Minimongo
- router: Flow Router
- build_tool: Meteor CLI

---

## Core Stack

- **Data**: DDP (Distributed Data Protocol).
- **DB**: MongoDB.

## Golden Snippet

```javascript
import { Meteor } from 'meteor/meteor';
Meteor.methods({
  'tasks.insert'(text) {
    check(text, String);
    Tasks.insert({ text });
  },
});
```
