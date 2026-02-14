---
tags: ["backend", "ruby", "fullstack"]
---
# Framework: Ruby on Rails

## Schema: Framework Specification

- framework: Ruby on Rails
- category: backend
- language: Ruby
- latest_supported_version: 8.0+
- rendering_engine: ERB/Hotwire
- state_management: ActiveRecord
- router: Rails Router
- build_tool: Bundler

---

## Core Stack

- **Gem**: `bundle` management.

## Golden Snippet

```ruby
class UsersController < ApplicationController
  def index
    @users = User.all
  end
end
```
