chrome-extension manifest文件详解
==================================

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2016-01-19 16:21:51
:status: draft
:tags: chrome, chrome-extension, chrome-manifest

manifest文件格式
----------------

manifest.json是chrome-extension的描述文件，是必须的, 并且要放到extension项目跟目录。
manifest使用json格式.

manifest实例
------------

如下是一个比较全的manifest文件实例，url来源: https://developer.chrome.com/extensions/manifest.
如果对某个属性不太了解可以去到上面的url，点击了解.
::

    {
      // Required
      "manifest_version": 2,
      "name": "My Extension",
      "version": "versionString",

      // Recommended
      "default_locale": "en",
      "description": "A plain text description",
      "icons": {...},

      // Pick one (or none)
      "browser_action": {...},
      "page_action": {...},

      // Optional
      "author": ...,
      "automation": ...,
      "background": {
        // Recommended
        "persistent": false
      },
      "background_page": ...,
      "chrome_settings_overrides": {...},
      "chrome_ui_overrides": {
        "bookmarks_ui": {
          "remove_bookmark_shortcut": true,
          "remove_button": true
        }
      },
      "chrome_url_overrides": {...},
      "commands": {...},
      "content_capabilities": ...,
      "content_scripts": [{...}],
      "content_security_policy": "policyString",
      "converted_from_user_script": ...,
      "copresence": ...,
      "current_locale": ...,
      "devtools_page": "devtools.html",
      "event_rules": [{...}],
      "externally_connectable": {
        "matches": ["*://*.example.com/*"]
      },
      "file_browser_handlers": [...],
      "file_system_provider_capabilities": {
        "configurable": true,
        "multiple_mounts": true,
        "source": "network"
      },
      "homepage_url": "http://path/to/homepage",
      "import": [{"id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}],
      "incognito": "spanning or split",
      "input_components": ...,
      "key": "publicKey",
      "minimum_chrome_version": "versionString",
      "nacl_modules": [...],
      "oauth2": ...,
      "offline_enabled": true,
      "omnibox": {
        "keyword": "aString"
      },
      "optional_permissions": ["tabs"],
      "options_page": "options.html",
      "options_ui": {
        "chrome_style": true,
        "page": "options.html"
      },
      "permissions": ["tabs"],
      "platforms": ...,
      "plugins": [...],
      "requirements": {...},
      "sandbox": [...],
      "short_name": "Short Name",
      "signature": ...,
      "spellcheck": ...,
      "storage": {
        "managed_schema": "schema.json"
      },
      "system_indicator": ...,
      "tts_engine": {...},
      "update_url": "http://path/to/updateInfo.xml",
      "version_name": "aString",
      "web_accessible_resources": [...]
    }

部分重要属性说明
----------------

:manifest_version: manifest格式的版本号，当前为2.

:name: extension名，显示用.

:version: extension版本号, 用于判断是否需要更新. 1.0.1

:description: extension描述,132字符内, 显示用.

:icons: 用于chrome使用的图片，需要有一个128x128/48x48/16x16, 最好使用png格式.格式如下

::

    "icons": {
        "16": "icon16.png",
        "48": "icon48.png",
        "128": "icon128.png"
    }

:browser_action: 用于在chrome工具栏放一个图标，可以附带文字和一个popup.html.
                 与page_action比须二选一, 始终可见.

:page_action: 基本同browser_action, 图片被放在地址栏最右边.

:background: 用于配置一个需要持续运行的后台任务.

:chrome_settings_overrides: 用于改写chrome的homepage/searchprovider/startpage等配置.

:chrome_ui_overrides: 用于改写chrome默认的界面显示，如bookmark的图标和快捷键.

:chrome_url_overrides: 可以用来改写bookmark-manager/history/new-tab页面。

:commands: 用来定义chrome快捷键, 可以定义为操作系统全局快捷键

**TODO**
