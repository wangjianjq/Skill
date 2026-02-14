---
tags: ["harmonyos", "ecosystem", "distributed", "modular"]
---
# Knowledge: HarmonyOS Ecosystem & Development

> **Latest Version**: HarmonyOS 6 (Released Oct 2025, API 21)  
> **Architecture**: 100% AOSP-free, pure HongMeng Kernel since HarmonyOS 6

## 📊 HarmonyOS 6 Key Improvements

* **Performance** (vs HarmonyOS 5):
  * Content loading: **↑30%**
  * App startup: **↑11%**
  * Page rendering: **↑21%**
  * Overall fluidity: **↑15%** (↑40% vs HarmonyOS 4)
  * Battery life: **+35-51 minutes**
* **Security**: StarShield Security Architecture (AI-driven, kernel-to-cloud)
* **AI Integration**: PanGu 5.5 models (NLP, CV, multi-modal)
* **Developer Experience**: One-time development, multi-device deployment
* **Ecosystem**: 100,000+ native apps (Q4 2025 target)

## 🏗️ Development Toolchain

### DevEco Studio

* **IDE**: Official HarmonyOS IDE (based on IntelliJ IDEA)
* **Version**: Use latest stable version (5.0+, HarmonyOS 6 support)
* **SDK Management**: `File` → `Settings` → `OpenHarmony SDK`
* **Emulator**: Built-in HarmonyOS emulator with multi-device profiles
* **Debugger**: ArkUI Inspector for real-time UI debugging
* **Performance**: SmartPerf for profiling (CPU, Memory, GPU)
* **AI Assistant**: Enhanced AI-assisted programming features (HarmonyOS 6)
* **Code Linter**: Static analysis tools for ArkTS/ArkUI

### Build System: Hvigor

* **Type**: Gradle-like build automation tool
* **Configuration**: `hvigorfile.ts` (TypeScript-based)
* **Tasks**: Compile, package, sign, deploy
* **Multi-target**: Support HAP/HAR/HSP building

### Project Structure

```text
MyHarmonyApp/
├── AppScope/                  # Global app config
│   └── app.json5             # App metadata
├── entry/                     # Main module (HAP)
│   ├── src/
│   │   └── main/
│   │       ├── ets/          # ArkTS source
│   │       │   ├── entryability/
│   │       │   │   └── EntryAbility.ts
│   │       │   └── pages/
│   │       │       └── Index.ets
│   │       ├── resources/    # Images, strings, etc.
│   │       └── module.json5  # Module config
│   └── build-profile.json5   # Build settings
├── common/                    # Shared HAR/HSP modules
└── hvigorfile.ts             # Build script
```

---

## 📦 Modular Development: HAR vs HSP

### HAR (Harmony Archive) - Static Shared Package

**Purpose**: Compile-time code reuse

**Characteristics**:

* **Static Linking**: Compiled into each HAP that references it
* **Code Duplication**: If multiple HAPs reference the same HAR, code is duplicated
* **No Independent Deployment**: Bundled with HAP at build time
* **Page Support**: Cannot declare pages in `main_pages.json` (export pages via methods)

**Use Cases**:

* Common utility libraries
* Shared UI components
* Base SDK modules
* When compile-time dependency is acceptable

#### Example: Creating HAR

```bash
# In DevEco Studio
File → New → Module → Static Library (HAR)
```

#### Export from HAR

```typescript
// In HAR module: index.ets
export { MyCustomComponent } from './components/MyCustomComponent';
export { UtilityClass } from './utils/UtilityClass';
```

#### Import in HAP

```typescript
import { MyCustomComponent } from '@ohos/my-har-library';
```

### HSP (Harmony Shared Package) - Dynamic Shared Package

**Purpose**: Runtime code sharing

**Characteristics**:

* **Dynamic Loading**: Loaded at runtime, code exists only once in memory
* **No Code Duplication**: Saves app size significantly
* **Runtime Dependency**: Installed alongside HAP but loaded on-demand
* **Page Support**: CAN declare pages in `main_pages.json`
* **Performance**: Lazy loading improves startup time

**Use Cases**:

* Large, infrequently used modules (e.g., advanced settings)
* Shared business logic across multiple feature HAPs
* When app size optimization is critical
* Cross-HAP resource sharing

#### Example: Creating HSP

```bash
# In DevEco Studio
File → New → Module → Shared Library (HSP)
```

#### Declare Page in HSP (module.json5)

```json
{
  "module": {
    "name": "featureModule",
    "type": "shared",
    "pages": "$profile:main_pages"
  }
}
```

#### Load HSP Page from HAP

```typescript
import { router } from '@kit.ArkUI';

router.pushUrl({
  url: '@bundle:com.example.myapp/featureModule/ets/pages/FeaturePage'
});
```

### HAP (Harmony Ability Package) - Application Unit

* **Definition**: Installable/runnable unit of HarmonyOS app
* **Types**:
  * **Entry**: Main app entry (icon on launcher)
  * **Feature**: Modular feature packages (loaded dynamically)
* **Composition**: Can reference multiple HAR/HSP modules
* **Deployment**: Bundled into App Pack (.app file) for distribution

### Comparison Table

| Feature | HAR | HSP | HAP |
|:--------|:----|:----|:----|

| **Type** | Static Library | Dynamic Library | App Package |
| **Code Duplication** | Yes (per HAP) | No (single copy) | N/A |
| **Page Declaration** | ❌ No | ✅ Yes | ✅ Yes |
| **Runtime Loading** | Compile-time | On-demand | Always loaded |
| **Use Case** | Utilities, Components | Large modules | App entry/features |
| **App Size Impact** | May increase | Optimized | N/A |

---

## 🌐 Distributed Capabilities (鸿蒙特色)

### Cross-Device Collaboration

**Capability Categories**:

1. **Distributed Data Management**: Sync app data across devices
2. **Distributed Task Scheduling**: Start/migrate tasks on other devices
3. **Distributed Device Virtualization**: Treat remote devices as local peripherals

**Example: Distributed Data (KVStore)**

```typescript
import distributedKVStore from '@ohos.data.distributedKVStore';

// Create distributed KV store
const kvManager = distributedKVStore.createKVManager({
  bundleName: 'com.example.myapp'
});

const kvStore = await kvManager.getKVStore('userPreferences', {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: true, // Auto-sync across devices
  kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION
});

// Put data (auto-syncs to connected devices)
await kvStore.put('theme', 'dark');

// Get data
const theme = await kvStore.get('theme');
```

**Example: Distributed Task Scheduling**

```typescript
import distributedMissionManager from '@ohos.distributedMissionManager';

// Continue task on another device
distributedMissionManager.continueMission({
  srcDeviceId: localDeviceId,
  dstDeviceId: targetDeviceId,
  missionId: currentMissionId,
  wantParam: {
    data: { pageIndex: 3 } // Pass state
  }
});
```

### Device Discovery & Connection

```typescript
import deviceManager from '@ohos.distributedDeviceManager';

// Init device manager
const dmInstance = deviceManager.createDeviceManager('com.example.myapp');

// Discover nearby devices
dmInstance.on('deviceFound', (device) => {
  console.info(`Found device: ${device.deviceName}`);
});

dmInstance.startDeviceDiscovery({
  subscribeId: 100,
  mode: 0x55, // Active discovery
  medium: 0 // Auto (BLE/WiFi)
});
```

---

## 🆕 HarmonyOS 6 Exclusive Features

### StarShield Security Architecture

**Overview**: AI-driven protection system spanning kernel to cloud, introduced in HarmonyOS 6.

**Key Features**:

1. **Family Anti-Fraud**
   * Alerts users to suspicious calls
   * Remote call termination
   * Synchronized flagged numbers across devices

2. **AI Anti-Fraud Protection**
   * Detects scam attempts in real-time
   * AI face-swap detection during video calls
   * Deep-fake voice recognition

3. **Anti-Peek Protection**
   * Automatically hides sensitive content when others view the screen
   * Context-aware privacy mode

4. **Encrypted Sharing**
   * End-to-end encryption for file/media sharing
   * Restrict access to approved recipients
   * Block screenshots/recordings of shared content

5. **App Installation Scrutiny**
   * 200+ detection capabilities in AppGallery
   * Continuous monitoring post-installation
   * Automatic blocking of harmful apps

**Example: Encrypted File Sharing**

```typescript
import fileShare from '@ohos.app.ability.fileShare';

// Share file with encryption
const shareOptions = {
  uri: 'file:///data/storage/el2/base/files/document.pdf',
  recipients: ['user@example.com'],
  encryption: true,
  expirationHours: 24,
  preventScreenshot: true
};

await fileShare.shareWithEncryption(shareOptions);
```

### PanGu AI Integration

**Overview**: HarmonyOS 6 integrates PanGu 5.5 AI models for intelligent features.

**Capabilities**:

* **Natural Language Processing (NLP)**
* **Computer Vision (CV)**
* **Multi-modal Interactions**
* **Scientific Computing**
* **Prediction & Knowledge Q&A**

**Example: AI Writing Assistant**

```typescript
import { aiAssistant } from '@kit.AIKit';

// Use AI writing assistant
const writerAPI = aiAssistant.getWriter();

const improvedText = await writerAPI.polish({
  originalText: 'User input text here',
  style: 'professional', // or 'casual', 'formal'
  language: 'en-US'
});

console.info('Improved:', improvedText);
```

**Example: Intelligent Data Retrieval**

```typescript
import { intelligentRetrieval } from '@kit.AIKit';

// Vector-based knowledge retrieval
const query = 'How to optimize battery life?';

const results = await intelligentRetrieval.search({
  query: query,
  vectorize: true,
  topK: 5,
  knowledgeBase: 'user-manual'
});

for (const result of results) {
  console.info(`Answer: ${result.content}, Score: ${result.relevance}`);
}
```

### Harmony Intelligence Agent Framework (HMAF)

**Purpose**: Multi-agent collaboration for complex tasks.

**Features**:

* Natural, efficient human-computer interaction
* Task decomposition across multiple intelligent agents
* Context-aware decision making

**Example: Multi-Agent Task**

```typescript
import { hmaf } from '@kit.AIKit';

// Create intelligent agent
const agent = hmaf.createAgent({
  name: 'ProductivityAssistant',
  capabilities: ['scheduling', 'email', 'reminder']
});

// Execute complex task
const result = await agent.execute({
  task: 'Schedule a meeting with John tomorrow at 2 PM and send him the agenda',
  context: {
    calendar: currentCalendar,
    contacts: userContacts
  }
});

console.info('Task completed:', result.summary);
```

---

## 🎯 System Capabilities & Permissions

### Permission Types

1. **Normal Permissions**: Auto-granted at install (e.g., Internet access)
2. **System Permissions**: Require user authorization (e.g., Camera, Location)
3. **StarShield Protected**: Enhanced AI-driven permission monitoring (HarmonyOS 6)

#### Declare in module.json5

```json
{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.CAMERA",
        "reason": "$string:camera_reason",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.LOCATION",
        "reason": "$string:location_reason",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "always"
        }
      }
    ]
  }
}
```

**Request at Runtime**:

```typescript
import abilityAccessCtrl from '@ohos.abilityAccessCtrl';
import { Permissions } from '@ohos.abilityAccessCtrl';

async function requestCameraPermission() {
  const atManager = abilityAccessCtrl.createAtManager();
  const permission: Permissions = 'ohos.permission.CAMERA';
  
  try {
    await atManager.requestPermissionsFromUser(context, [permission]);
    // Permission granted
  } catch (err) {
    // Permission denied
  }
}
```

### Common System APIs

| Capability | Module | Use Case |
|:-----------|:-------|:---------|

| **Camera** | `@ohos.multimedia.camera` | Photo/Video capture |
| **Location** | `@ohos.geoLocationManager` | GPS/Network positioning |
| **Notification** | `@ohos.notificationManager` | Push notifications |
| **Network** | `@ohos.net.http` | HTTP requests |
| **File I/O** | `@ohos.file.fs` | Read/write files |
| **Database** | `@ohos.data.relationalStore` | SQLite operations |
| **Preferences** | `@ohos.data.preferences` | Key-value storage |

---

## 🧪 Testing Framework

### 1. Unit Testing (Hypium)

**Framework**: `@ohos.hypium` (Official test framework)

**Example Test**:

```typescript
import { describe, it, expect } from '@ohos/hypium';
import { Calculator } from '../src/Calculator';

export default function calculatorTest() {
  describe('Calculator Test Suite', () => {
    it('should add two numbers correctly', () => {
      const calc = new Calculator();
      expect(calc.add(2, 3)).assertEqual(5);
    });
    
    it('should handle negative numbers', () => {
      const calc = new Calculator();
      expect(calc.add(-5, 3)).assertEqual(-2);
    });
  });
}
```

**Run Tests**:

```bash
# In DevEco Studio
Run → Edit Configurations → Add 'OpenHarmony Test' → Select test file
```

### 2. UI Testing (UiTest)

**Framework**: `@ohos.UiTest`

**Example UI Test**:

```typescript
import { Driver, ON, Component } from '@ohos.UiTest';

describe('UI Test Suite', () => {
  it('should click login button', async () => {
    const driver = Driver.create();
    
    // Find button by text
    const loginBtn = await driver.findComponent(ON.text('Login'));
    
    // Check existence
    expect(await loginBtn.isEnabled()).assertTrue();
    
    // Click
    await loginBtn.click();
    
    // Verify navigation
    const welcomeText = await driver.findComponent(ON.text('Welcome'));
    expect(await welcomeText.isClickable()).assertFalse();
  });
});
```

### 3. Performance Testing (SmartPerf)

**Tool**: Built into DevEco Studio

**Metrics**:

* CPU usage
* Memory consumption
* Frame rate (FPS)
* Render time
* Network latency

**Usage**: `View` → `Tool Windows` → `SmartPerf-Device`

---

## 🚨 Critical Development Rules

1. **Version Targeting**: Always target HarmonyOS 6 (API 21) for new projects
2. **No Android Deps**: HarmonyOS 6 is 100% AOSP-free (pure native)
3. **Modular Design**: Use HSP for large modules to optimize app size
4. **Distributed First**: Design with multi-device scenarios in mind
5. **Permission Privacy**: Request permissions only when needed (runtime, not at startup)
6. **Testing Coverage**: Maintain 80%+ code coverage with Hypium tests
7. **i18n Mandatory**: Use `$r()` for ALL user-facing strings
8. **Performance Budget**: Keep cold start time under 1.5s (HarmonyOS 6: 11% faster)
9. **Accessibility**: Implement screen reader support for all interactive elements
10. **Signature**: Configure automatic signing in DevEco Studio for device testing
11. **AI Integration**: Leverage PanGu AI APIs for intelligent features
12. **StarShield Security**: Implement encrypted sharing and anti-fraud features

---

## 📚 Official Resources

* **Developer Portal**: [https://developer.huawei.com/consumer/cn/harmonyos](https://developer.huawei.com/consumer/cn/harmonyos)
* **API Reference**: [https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/development-intro-V5](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/development-intro-V5)
* **Sample Code**: [https://gitee.com/harmonyos](https://gitee.com/harmonyos)
* **DevEco Studio Download**: [https://developer.huawei.com/consumer/cn/deveco-studio](https://developer.huawei.com/consumer/cn/deveco-studio)
