---
tags: ["miniprogram", "wechat", "mobile"]
---
# FW: WeChat Mini Program (微信小程序)

## Schema: Framework Specification

- framework: WeChat Mini Program
- category: mobile
- language: JavaScript/TypeScript
- latest_supported_version: 基础库 v3.5+
- rendering_engine: Skyline (60fps native rendering)
- state_management: MobX/Pinia/Zustand
- router: Navigator API
- build_tool: WeChat DevTools | Uni-app | Taro

---

> **Protocol**: WeChat Mini Program Development Standard  
> **Version Coverage**: 微信开发者工具 v1.06+ / 基础库 v3.x (Modern) | 基础库 v2.x (Legacy)

---

## Version Strategy (版本策略)

### 🟢 Modern Track (现代路线) — **RECOMMENDED**

**Target**: 基础库 v3.5.0+ (2025年起), Skyline 渲染引擎, AI 能力集成  
**IDE**: 微信开发者工具 Stable Channel v1.06.2501120+  
**Language**: JavaScript ES6+ / TypeScript 5.0+  
**Rendering**: Skyline 渲染引擎 (60fps, 原生渲染)  
**Component Framework**: Glass-easel v2.0+  
**State Management**: MobX 6+ / Pinia (Uni-app) / Zustand (Taro)  
**AI Integration**: 微信 AI API (智能客服、图像识别、NLP)

### 🟡 Legacy Track (遗留支持)

**Target**: 基础库 v2.x (2023年前项目)  
**Rendering**: WebView 渲染  
**Component Framework**: Component v1.x  
**State Management**: 原生 setData / 全局变量

---

## Core Stack (核心技术栈)

### 1. Native WeChat Mini Program (原生微信小程序)

```javascript
// app.json - 全局配置
{
  "pages": [
    "pages/index/index",
    "pages/detail/detail"
  ],
  "window": {
    "navigationBarTitleText": "小程序标题",
    "navigationBarBackgroundColor": "#ffffff",
    "renderer": "skyline",  // 使用 Skyline 渲染引擎
    "rendererOptions": {
      "skyline": {
        "defaultDisplayBlock": true
      }
    }
  },
  "lazyCodeLoading": "requiredComponents",  // 按需注入
  "useExtendedLib": {
    "weui": true  // 使用 WeUI 扩展库
  },
  "permission": {
    "scope.userLocation": {
      "desc": "您的位置信息将用于小程序位置接口的效果展示"
    }
  }
}
```

```xml
<!-- pages/index/index.wxml - 页面结构 -->
<view class="container">
  <text class="title">{{title}}</text>
  <button bindtap="onButtonClick">点击</button>
  
  <!-- 使用 WXS 增强视图层能力 -->
  <wxs module="utils">
    var formatTime = function(timestamp) {
      var date = getDate(timestamp);
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
    }
    module.exports.formatTime = formatTime;
  </wxs>
  
  <text>创建时间: {{utils.formatTime(createTime)}}</text>
</view>
```

```css
/* pages/index/index.wxss - 样式 */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.title {
  font-size: 48rpx;  /* rpx 响应式单位,自适应屏幕宽度 */
  color: #ffffff;
  margin-bottom: 40rpx;
}
```

```javascript
// pages/index/index.js - 逻辑层
Page({
  data: {
    title: '欢迎使用微信小程序',
    createTime: Date.now()
  },
  
  onLoad(options) {
    // 获取用户信息 (需用户授权)
    this.getUserProfile();
  },
  
  async getUserProfile() {
    try {
      const res = await wx.getUserProfile({
        desc: '用于完善会员资料'
      });
      this.setData({
        userInfo: res.userInfo
      });
    } catch (err) {
      console.error('用户拒绝授权', err);
    }
  },
  
  onButtonClick() {
    wx.navigateTo({
      url: '/pages/detail/detail?id=123'
    });
  }
});
```

### 2. Uni-app (Vue 跨端框架)

**优势**: 一次开发,生成微信/支付宝/百度/抖音小程序 + H5 + App

```vue
<!-- pages/index/index.vue -->
<template>
  <view class="container">
    <text class="title">{{ title }}</text>
    <button @click="navigateToDetail">进入详情</button>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const title = ref('Uni-app 微信小程序');

const navigateToDetail = () => {
  uni.navigateTo({
    url: '/pages/detail/detail?id=123'
  });
};

// 使用 Pinia 状态管理 (推荐)
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.title {
  font-size: 48rpx;
  color: #333;
}
</style>
```

```json
// manifest.json - Uni-app 配置
{
  "mp-weixin": {
    "appid": "wx1234567890abcdef",
    "setting": {
      "urlCheck": true,
      "es6": true,
      "minified": true,
      "lazyCodeLoading": "requiredComponents"
    },
    "usingComponents": true,
    "renderer": "skyline",
    "optimization": {
      "subPackages": true
    }
  }
}
```

### 3. Taro (React/TypeScript 跨端框架)

**优势**: React 语法,适合 React 技术栈团队

```tsx
// pages/index/index.tsx
import { View, Text, Button } from '@tarojs/components';
import { useState } from 'react';
import Taro from '@tarojs/taro';
import './index.scss';

export default function Index() {
  const [title, setTitle] = useState('Taro 微信小程序');
  
  const navigateToDetail = () => {
    Taro.navigateTo({
      url: '/pages/detail/detail?id=123'
    });
  };
  
  return (
    <View className="container">
      <Text className="title">{title}</Text>
      <Button onClick={navigateToDetail}>进入详情</Button>
    </View>
  );
}
```

```typescript
// config/index.ts - Taro 配置
export default {
  projectName: 'taro-miniprogram',
  framework: 'react',
  compiler: {
    type: 'webpack5'
  },
  mini: {
    skylineRenderEnable: true,  // 启用 Skyline 渲染
    lazyCodeLoading: 'requiredComponents',
    compile: {
      exclude: [/node_modules/]
    }
  }
};
```

---

## Performance Optimization (性能优化)

### 1. 分包加载 (Subpackages)

```json
// app.json - 分包配置
{
  "pages": ["pages/index/index"],
  "subPackages": [
    {
      "root": "subpkg/shop",
      "pages": ["pages/list/list", "pages/detail/detail"],
      "independent": false  // 普通分包
    },
    {
      "root": "subpkg/user",
      "pages": ["pages/profile/profile"],
      "independent": true   // 独立分包,可独立运行
    }
  ],
  "preloadRule": {
    "pages/index/index": {
      "network": "all",
      "packages": ["subpkg/shop"]  // 预下载分包
    }
  }
}
```

### 2. 图片优化

```javascript
// 图片压缩与懒加载
<image 
  src="{{imgUrl}}" 
  mode="aspectFill"
  lazy-load="{{true}}"
  webp="{{true}}"  // 优先使用 WebP 格式
  show-menu-by-longpress="{{true}}"
/>
```

### 3. setData 优化

```javascript
// ❌ 错误: 频繁 setData
for (let i = 0; i < 100; i++) {
  this.setData({ [`list[${i}]`]: data[i] });  // 触发 100 次渲染
}

// ✅ 正确: 批量更新
const updates = {};
for (let i = 0; i < 100; i++) {
  updates[`list[${i}]`] = data[i];
}
this.setData(updates);  // 只触发 1 次渲染
```

### 4. Worklet 动画 (Skyline 专属)

```javascript
// 高性能手势动画
const worklet = requireWorklet('./animation.js');

this.applyAnimatedStyle('.box', () => {
  'worklet';
  return {
    transform: `translateX(${shared.offset}px)`
  };
});
```

---

## WeChat AI Integration (微信 AI 能力集成)

### 2026年微信 AI 成长计划

微信提供免费算力、流量扶持,支持 AI 应用快速上线。

```javascript
// 1. AI 智能客服
wx.cloud.callFunction({
  name: 'aiChat',
  data: {
    prompt: '用户问题',
    context: conversationHistory
  }
}).then(res => {
  console.log('AI 回复:', res.result.answer);
});

// 2. 图像识别 (OCR、物体检测)
wx.chooseImage({
  success: async (res) => {
    const tempFilePath = res.tempFilePaths[0];
    const aiResult = await wx.cloud.callFunction({
      name: 'imageRecognition',
      data: { imageUrl: tempFilePath }
    });
    console.log('识别结果:', aiResult.result.labels);
  }
});

// 3. 智能推荐
wx.cloud.callFunction({
  name: 'aiRecommend',
  data: {
    userId: this.data.userId,
    behavior: userBehaviorLog
  }
}).then(res => {
  this.setData({ recommendations: res.result.items });
});
```

---

## WeChat Pay (微信支付)

```javascript
// 统一下单 + 支付
wx.cloud.callFunction({
  name: 'pay',
  data: {
    amount: 9900,  // 单位: 分 (99.00元)
    description: '商品购买'
  }
}).then(res => {
  const { payment } = res.result;
  
  wx.requestPayment({
    timeStamp: payment.timeStamp,
    nonceStr: payment.nonceStr,
    package: payment.package,
    signType: 'RSA',
    paySign: payment.paySign,
    success: () => {
      wx.showToast({ title: '支付成功', icon: 'success' });
    },
    fail: (err) => {
      console.error('支付失败', err);
    }
  });
});
```

---

## Security & Compliance (安全与合规)

### 1. HTTPS 强制要求

所有网络请求必须使用 HTTPS:

```javascript
// ✅ 正确
wx.request({
  url: 'https://api.example.com/data',  // 必须 HTTPS
  success: (res) => console.log(res.data)
});

// ❌ 错误
wx.request({
  url: 'http://api.example.com/data',  // HTTP 会被拦截
});
```

### 2. 域名白名单配置

在小程序管理后台 → 开发 → 开发管理 → 服务器域名,添加:

- **request 合法域名**: `https://api.example.com`
- **uploadFile 合法域名**: `https://upload.example.com`
- **downloadFile 合法域名**: `https://download.example.com`

### 3. ICP 备案 (强制要求)

**2026年起所有小程序必须完成**:

1. **ICP 备案** (Internet Content Provider Filing)
2. **小程序备案** (Mini Program Filing)

未备案小程序将无法上架。

### 4. 数据安全

```javascript
// 敏感数据加密传输
const encryptedData = wx.getStorageSync('userToken');
wx.cloud.callFunction({
  name: 'secureAPI',
  data: {
    token: encryptedData,
    timestamp: Date.now(),
    signature: generateSignature(encryptedData)  // HMAC-SHA256
  }
});
```

---

## Testing (测试)

### 1. 单元测试 (Jest)

```javascript
// __tests__/utils.test.js
import { formatPrice } from '../utils/format';

describe('formatPrice', () => {
  it('should format price correctly', () => {
    expect(formatPrice(9900)).toBe('¥99.00');
    expect(formatPrice(12345)).toBe('¥123.45');
  });
});
```

### 2. 真机调试

```bash
# 微信开发者工具
1. 点击 "预览" 生成二维码
2. 用微信扫码在真机上打开
3. 开启 "调试模式" 查看 vConsole 日志
```

---

## Deployment & Release (部署与发布)

### 1. 版本管理

```json
// 遵循语义化版本
{
  "version": "1.2.3",
  "description": "v1.2.3 - 新增 AI 客服功能,修复支付问题"
}
```

### 2. 发布流程

```bash
# 步骤 1: 上传代码
微信开发者工具 → 上传 → 填写版本号和备注

# 步骤 2: 提交审核
小程序管理后台 → 版本管理 → 开发版本 → 提交审核

# 步骤 3: 审核通过后发布
审核通过 → 全量发布 / 分阶段发布 (灰度)
```

---

## Golden Snippet (黄金代码片段)

```javascript
// pages/index/index.js - 原生微信小程序完整示例
Page({
  data: {
    userInfo: null,
    products: [],
    loading: false
  },
  
  onLoad() {
    this.loadProducts();
  },
  
  // 加载商品列表
  async loadProducts() {
    this.setData({ loading: true });
    
    try {
      const res = await wx.cloud.database().collection('products')
        .where({ status: 'active' })
        .orderBy('createTime', 'desc')
        .limit(20)
        .get();
      
      this.setData({ 
        products: res.data,
        loading: false 
      });
    } catch (err) {
      wx.showToast({ title: '加载失败', icon: 'error' });
      this.setData({ loading: false });
    }
  },
  
  // 获取用户信息 (需授权)
  async getUserProfile() {
    try {
      const res = await wx.getUserProfile({
        desc: '用于完善会员资料'
      });
      
      this.setData({ userInfo: res.userInfo });
      
      // 保存用户信息到数据库
      await wx.cloud.database().collection('users').add({
        data: {
          ...res.userInfo,
          createTime: new Date()
        }
      });
    } catch (err) {
      console.error('用户取消授权', err);
    }
  },
  
  // 商品详情跳转
  onProductTap(e) {
    const { id } = e.currentTarget.dataset;
    wx.navigateTo({
      url: `/pages/detail/detail?id=${id}`
    });
  },
  
  // 分享配置
  onShareAppMessage() {
    return {
      title: '发现好物,快来看看',
      path: '/pages/index/index',
      imageUrl: '/images/share-cover.jpg'
    };
  },
  
  // 分享到朋友圈
  onShareTimeline() {
    return {
      title: '精选好物推荐',
      query: 'from=timeline'
    };
  }
});
```

---

## Best Practices (最佳实践)

### ✅ DO (推荐做法)

1. **使用 Skyline 渲染引擎** - 60fps 性能保证
2. **分包加载** - 首屏加载时间 < 2秒
3. **图片使用 WebP** - 体积比 PNG 小 30-50%
4. **启用懒加载** - `lazy-load="true"` 减少初次渲染压力
5. **AI 能力集成** - 利用微信 2026 免费算力计划
6. **TypeScript** - 提升代码可维护性
7. **云开发** - 免服务器部署,降低成本
8. **订阅消息** - 用户留存与召回

### ❌ DON'T (禁止做法)

1. ❌ 频繁 `setData` - 导致卡顿,批量更新
2. ❌ 使用 HTTP - 必须 HTTPS
3. ❌ 忽略 ICP 备案 - 2026年强制要求
4. ❌ 硬编码敏感信息 - 使用环境变量
5. ❌ 不做错误处理 - 所有 API 调用需 try-catch
6. ❌ 超大包体积 - 主包 < 2MB,总包 < 20MB
7. ❌ 阻塞主线程 - 复杂计算使用 Worker
8. ❌ 不测试真机 - 开发者工具不等于真实环境

---

## Resources (资源)

- 📖 [微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/)
- 🔧 [微信开发者工具下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)
- 🎨 [WeUI 组件库](https://github.com/Tencent/weui-wxss)
- 🚀 [Uni-app 官网](https://uniapp.dcloud.io/)
- ⚛️ [Taro 官网](https://taro.jd.com/)
- 🤖 [微信 AI 能力文档](https://developers.weixin.qq.com/miniprogram/dev/framework/ai/)
- 💳 [微信支付接入指南](https://pay.weixin.qq.com/wiki/doc/apiv3/index.shtml)

---

## Migration Guide (迁移指南)

### 从 H5 迁移到小程序

```javascript
// H5 代码
window.location.href = '/detail?id=123';
localStorage.setItem('token', 'xxx');
document.querySelector('.box').style.color = 'red';

// 小程序代码
wx.navigateTo({ url: '/pages/detail/detail?id=123' });
wx.setStorageSync('token', 'xxx');
this.setData({ boxColor: 'red' });  // 通过 data 绑定样式
```

### 从 React Native 迁移到小程序 (使用 Taro)

```tsx
// React Native
import { View, Text, TouchableOpacity } from 'react-native';

// Taro (几乎一致)
import { View, Text, Button } from '@tarojs/components';
```

---

## Version History (版本历史)

- **v3.5.0** (2025-10): Skyline 渲染引擎优化,AI 能力增强
- **v3.0.0** (2024-06): Skyline 正式版,Worklet 动画系统
- **v2.33.0** (2023-12): Glass-easel 组件框架
- **v2.0.0** (2020-01): 基础库重构,性能优化
