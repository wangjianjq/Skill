---
tags: ["ui", "harmonyos", "declarative", "cross-device"]
---
# Framework: ArkUI (HarmonyOS UI Framework)

## Schema: Framework Specification

- framework: ArkUI
- category: mobile
- language: ArkTS
- latest_supported_version: HarmonyOS 6 (API 21)
- rendering_engine: Ark Engine
- state_management: @State/@ObservedV2
- router: Navigation + Router API
- build_tool: DevEco Studio

---

## [Modern] (HarmonyOS 6 / HarmonyOS Next 5.0+)

> **Latest**: HarmonyOS 6 (API 21) - Released Oct 2025

- **Paradigm**: Declarative UI (similar to SwiftUI/Jetpack Compose)
- **Rendering**: Ark Engine with hardware acceleration (60+ FPS guaranteed)
- **State Management**:
  - **Simple**: `@State`, `@Prop`, `@Link`
  - **Complex**: `@ObservedV2` + `@Trace` (State Management V2)
  - **Global**: `@Provide` + `@Consume`, `AppStorage`
- **Lists**: `LazyForEach` for performance optimization
- **Navigation**: `Navigation` component + `Router` API
- **AI Integration**: PanGu AI-powered components (Writing Assistant, Video Generation)

### HarmonyOS 6 UI Enhancements

- **ArkUI Component Upgrades**: New C APIs for attribute styles, enhanced SVG parsing
- **Performance**: 21% faster page rendering, 15% overall fluidity boost
- **Visual Refinements**: Updated animations, dynamic light-sensing system
- **Cross-Device**: Seamless task continuation across phones/tablets/PCs
- **Chromium 132**: ArkWeb kernel upgraded for better web compatibility

### Component Architecture

- **Built-in Components**: `Text`, `Button`, `Image`, `List`, `Grid`, `Swiper`, etc.
- **Container Components**: `Column`, `Row`, `Stack`, `Flex`, `Scroll`
- **Custom Components**: Use `@Component` decorator with `struct` keyword

### Modern Snippet: Complete UI Example

```typescript
import { router } from '@kit.ArkUI';

interface TodoItem {
  id: number;
  title: string;
  completed: boolean;
}

@Entry
@Component
struct TodoListPage {
  @State todos: TodoItem[] = [
    { id: 1, title: 'Learn ArkTS', completed: false },
    { id: 2, title: 'Build HarmonyOS App', completed: false }
  ];
  @State newTodoText: string = '';

  build() {
    Column({ space: 16 }) {
      // Header
      Text('Todo List')
        .fontSize(28)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 20, bottom: 10 })
      
      // Input Row
      Row({ space: 10 }) {
        TextInput({ placeholder: 'Enter new todo' })
          .layoutWeight(1)
          .onChange((value: string) => {
            this.newTodoText = value;
          })
        
        Button('Add')
          .onClick(() => {
            if (this.newTodoText.trim()) {
              this.todos.push({
                id: Date.now(),
                title: this.newTodoText,
                completed: false
              });
              this.newTodoText = '';
            }
          })
      }
      .width('90%')
      
      // List
      List({ space: 8 }) {
        LazyForEach(new TodoDataSource(this.todos), (item: TodoItem) => {
          ListItem() {
            this.TodoItemCard(item)
          }
        }, (item: TodoItem) => item.id.toString())
      }
      .layoutWeight(1)
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F5F5F5')
  }
  
  @Builder
  TodoItemCard(item: TodoItem) {
    Row({ space: 12 }) {
      Checkbox({ name: item.id.toString(), group: 'todoGroup' })
        .select(item.completed)
        .onChange((isChecked: boolean) => {
          const index = this.todos.findIndex(t => t.id === item.id);
          if (index !== -1) {
            this.todos[index].completed = isChecked;
          }
        })
      
      Text(item.title)
        .fontSize(16)
        .decoration({ type: item.completed ? TextDecorationType.LineThrough : TextDecorationType.None })
        .layoutWeight(1)
    }
    .width('100%')
    .padding(12)
    .backgroundColor(Color.White)
    .borderRadius(8)
  }
}

// DataSource for LazyForEach
class TodoDataSource implements IDataSource {
  private data: TodoItem[];
  
  constructor(data: TodoItem[]) {
    this.data = data;
  }
  
  totalCount(): number {
    return this.data.length;
  }
  
  getData(index: number): TodoItem {
    return this.data[index];
  }
  
  registerDataChangeListener(listener: DataChangeListener): void {}
  
  unregisterDataChangeListener(listener: DataChangeListener): void {}
}
```

### State Management Patterns

#### 1. Local State (`@State`)

```typescript
@Component
struct Counter {
  @State count: number = 0;
  
  build() {
    Text(`Count: ${this.count}`)
  }
}
```

#### 2. Parent-Child Communication (`@Prop` + `@Link`)

```typescript
@Component
struct Parent {
  @State sharedValue: string = 'Hello';
  
  build() {
    Column() {
      // One-way (parent -> child)
      ChildWithProp({ value: this.sharedValue })
      
      // Two-way (parent <-> child)
      ChildWithLink({ value: $sharedValue })
    }
  }
}

@Component
struct ChildWithProp {
  @Prop value: string;
  
  build() {
    Text(this.value) // Read-only
  }
}

@Component
struct ChildWithLink {
  @Link value: string;
  
  build() {
    TextInput({ text: this.value })
      .onChange((text: string) => {
        this.value = text; // Updates parent state
      })
  }
}
```

#### 3. Global State (`@Provide` + `@Consume`)

```typescript
@Entry
@Component
struct App {
  @Provide('theme') currentTheme: string = 'dark';
  
  build() {
    Column() {
      DeepNestedComponent()
    }
  }
}

@Component
struct DeepNestedComponent {
  @Consume('theme') currentTheme: string;
  
  build() {
    Text(`Theme: ${this.currentTheme}`)
  }
}
```

### Navigation Patterns

#### Router API (Page Jumping)

```typescript
import { router } from '@kit.ArkUI';

// Navigate to new page
router.pushUrl({
  url: 'pages/DetailPage',
  params: { id: 123, name: 'Item' }
});

// Navigate back
router.back();

// Retrieve params in target page
const params = router.getParams() as Record<string, Object>;
const itemId = params['id'] as number;
```

### Performance Optimization (HarmonyOS 6)

- **LazyForEach**: MANDATORY for lists with 50+ items
- **@Builder**: Extract reusable UI blocks to improve modularity
- **Conditional Rendering**: Use `if/else` sparingly, prefer visibility control
- **Component Reuse**: Enable `reusable: true` for frequently created/destroyed components
- **Image Optimization**: Use `Image.cached(true)` for static images
- **Ark Engine Optimization**: Leverage 30% content loading speed improvement
- **60+ FPS Target**: Design for smooth animations with Ark Compiler AOT compilation
- **Memory Efficiency**: Utilize improved GC for better resource management

### Responsive Layout (Multi-Device Adaptation)

```typescript
@Entry
@Component
struct ResponsivePage {
  @State windowWidth: number = 0;
  
  aboutToAppear() {
    // Get window size
    this.windowWidth = display.getDefaultDisplaySync().width;
  }
  
  build() {
    GridRow({
      columns: { xs: 4, sm: 8, md: 12, lg: 12 },
      gutter: { x: 8, y: 8 }
    }) {
      GridCol({ span: { xs: 4, sm: 4, md: 6, lg: 3 } }) {
        Text('Responsive Item 1')
      }
      GridCol({ span: { xs: 4, sm: 4, md: 6, lg: 3 } }) {
        Text('Responsive Item 2')
      }
    }
  }
}
```

## [Legacy] (HarmonyOS 2.x/3.x)

- **UI Model**: FAAbility or XML-based layouts (deprecated)
- **State**: Manual state management without decorators
- **Architecture**: Fragment-like navigation

---

## 🚨 Critical Rules

1. **NO Hardcoded Strings**: Use resource references `$r('app.string.xxx')`
2. **NO console.log**: Use `hilog` for all logging
3. **LazyForEach for Long Lists**: Lists with 50+ items MUST use `LazyForEach`
4. **Lifecycle Management**: Always clean up listeners in `aboutToDisappear()`
5. **Multi-Device Adaptation**: Use `GridRow`/`GridCol` for responsive layouts
6. **Accessibility**: Add `accessibilityText()` for all interactive components
7. **Dark Mode**: Use system colors or CSS variables for theme adaptation

## 🎨 Design Standards

Integrate with HarmonyOS Design language:

- **Spacing**: Use 4px/8px/16px/24px grid system
- **Colors**: Leverage `$r('sys.color.xxx')` for system colors
- **Typography**: Follow HarmonyOS font scales (14/16/18/24/28)
- **Motion**: Use `animateTo()` with standard curves (cubic-bezier)
