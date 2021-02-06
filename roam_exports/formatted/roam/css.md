- Better Roam Research Theme
    - ```css
:root {
  --font-size: 15.5px;
  --c1: hsl(206, 10%, 16%);
  --c2: hsl(206, 12%, 40%);
  --c3: hsl(206, 16%, 60%);
  --c4: hsl(206, 18%, 70%);
  --c5: hsl(206, 20%, 87%);
  --accent-color: hsl(203, 74%, 42%);
  --selection-color: hsl(203, 100%, 74%);
  --ref-hover-bg-color: hsl(204, 33%, 97%);
  --border-color: rgba(0, 0, 0, 0.12);
  --subtle-border-color: rgba(0, 0, 0, 0.07);
  --search-border-color: rgba(0, 0, 0, 0.07);
  --page-background-color: hsl(210, 9%, 98%);
  --main-area-background-color: [ffffff](<../ffffff.md>);
  --cards-background-color: [ffffff](<../ffffff.md>);
  --secondary-background-color: hsl(210, 14%, 96%);
  --popup-background-color: [ffffff](<../ffffff.md>);
  --reference-item-background: hsl(0, 0%, 99%);
  --brackets-color: rgba(0, 0, 0, 0.25);
  --empty-text-color: hsl(203, 12%, 75%);
}

body,
.roam-body,
.roam-app,
.rm-pages-title-text {
  color: var(--c1) !important;
}

.roam-app > div:only-child:not(.roam-sidebar-container) {
  margin-left: 0 !important;
}

.bp3-button:not(.bp3-intent-primary) {
  color: var(--c2) !important;
}

html,
body,
[app](<../app.md>) {
  background: var(--page-background-color) !important;
}


.roam-center,
.roam-body-main {
  border-left: 1px solid var(--subtle-border-color) !important;
  border-top: 1px solid var(--subtle-border-color) !important;
  border-right: 1px solid var(--subtle-border-color) !important;
  border-radius: 12px 12px 0 0;
  box-shadow: 0px 3px 20px rgba(0, 0, 0, 0.03) !important;
  background: var(--main-area-background-color) !important;
  margin-right: 8px;
  margin-left: 8px;
}
@media (max-width: 640px) {
  .roam-center,
.roam-body-main {
    margin-right: 6px;
    margin-left: 6px;
  }
}
.roam-center .roam-article,
.roam-body-main .roam-article {
  padding: 16px 32px 120px !important;
}
@media (max-width: 860px) {
  .roam-center .roam-article,
.roam-body-main .roam-article {
    padding: 12px 28px 120px !important;
  }
}
@media (max-width: 640px) {
  .roam-center .roam-article,
.roam-body-main .roam-article {
    padding: 10px 20px 120px !important;
  }
}

.roam-topbar {
  background: var(--page-background-color) !important;
  border-bottom: none !important;
}
.roam-topbar input[find-or-create-input](<../find-or-create-input.md>) {
  box-shadow: none !important;
  border: 1px solid var(--search-border-color) !important;
}

.roam-body,
.roam-topbar,
[right-sidebar](<../right-sidebar.md>),
.roam-sidebar-container {
  background: var(--page-background-color) !important;
  box-shadow: none !important;
}

.rm-quick-capture-sync-modal {
  background: var(--secondary-background-color) !important;
  border-radius: 8px !important;
}

[right-sidebar](<../right-sidebar.md>) {
  border: none !important;
  transition: none !important;
  overflow: hidden !important;
}
[right-sidebar](<../right-sidebar.md>) h1 {
  font-size: 18px !important;
}
[right-sidebar](<../right-sidebar.md>) [roam-right-sidebar-content](<../roam-right-sidebar-content.md>) {
  margin-left: -6px !important;
}
[right-sidebar](<../right-sidebar.md>) [roam-right-sidebar-content](<../roam-right-sidebar-content.md>) > div[style] {
  border-bottom: 1px solid var(--subtle-border-color) !important;
}
[right-sidebar](<../right-sidebar.md>) .hoverparent,
[right-sidebar](<../right-sidebar.md>) .react-resizable {
  max-width: 100% !important;
}
[right-sidebar](<../right-sidebar.md>) .hoverparent img,
[right-sidebar](<../right-sidebar.md>) .react-resizable img {
  max-width: 100% !important;
}
[right-sidebar](<../right-sidebar.md>) .rm-block-text {
  font-size: 14.5px !important;
}

.rm-title-display,
.rm-title-textarea,
.roam-log-page h1.level2 {
  height: auto !important;
  line-height: 1.5 !important;
  font-size: 26px !important;
  font-weight: 600 !important;
}

.rm-heading-level-1 > .rm-block-main span {
  margin-top: -2px !important;
}
.rm-heading-level-1 > .rm-block-main div,
.rm-heading-level-1 > .rm-block-main textarea {
  font-size: 22px !important;
  line-height: 1.5 !important;
  font-weight: 600 !important;
}

.rm-heading-level-2 > .rm-block-main span {
  margin-top: -2px !important;
}
.rm-heading-level-2 > .rm-block-main div,
.rm-heading-level-2 > .rm-block-main textarea {
  font-size: 20px !important;
  line-height: 1.5 !important;
  font-weight: 600 !important;
}

.rm-heading-level-3 > .rm-block-main span {
  margin-top: -1px !important;
  color: var(--c2) !important;
}
.rm-heading-level-3 > .rm-block-main div,
.rm-heading-level-3 > .rm-block-main textarea {
  color: var(--c2) !important;
  font-size: 18px !important;
  line-height: 1.5 !important;
}

.level2 {
  font-weight: inherit !important;
}

h1 {
  color: var(--c1) !important;
}

div.roam-article span > a.rm-alias--external:after {
  content: "";
  display: inline-block;
  object-fit: cover;
  mask-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAABYlAAAWJQFJUiTwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAGDSURBVHgBtZaNcYMwDIUfGzgbqBuUDcwkaTdoJ4AN0gmaTNJu0GyQdILSCUjRIa6yMT+x4d29O7CNPmMLmQzryYhZ39hIDChbX1vflPn+2JqwoigA8t20fsEKogCslrZ6C6iG/UhAo/qLwBhCpCzc2T+OjNu1PquxB0TqpIK8e33k3Rdw3zJKnyqIVe2VtF1UW4b/PW0QuawaaDyYH5iBVyQCSQA2ALvJPRRQT8QgUdUEjPWs+r6QqHIGlsPdv/1UMIuuNJ3Fh4UwI8+WcAvAZQxEcJNCm2ZgOYZVpodRCPaAYblqxP0MK4wv42sA9oGJzPRLEQez8oDBfILwhHl1eAuOcL/RgZ48mF+uqhnY3dI1b781zHgBl8AKuSZEiOCe1KF2P/V1UiQBa6+Ps7OBu4w2FQi4308RmJDWCePH02K9qSCcQLuRcTncZbaIFKH7HPRe8ptmYp4A/0bUCO93lDhgg2U/RqPlag3o4toYK0JXmvoM1fW0QuIhmmEezvoVJ+sPourrpWEel2gAAAAASUVORK5CYII=");
  -webkit-mask-box-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAACXBIWXMAABYlAAAWJQFJUiTwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAGDSURBVHgBtZaNcYMwDIUfGzgbqBuUDcwkaTdoJ4AN0gmaTNJu0GyQdILSCUjRIa6yMT+x4d29O7CNPmMLmQzryYhZ39hIDChbX1vflPn+2JqwoigA8t20fsEKogCslrZ6C6iG/UhAo/qLwBhCpCzc2T+OjNu1PquxB0TqpIK8e33k3Rdw3zJKnyqIVe2VtF1UW4b/PW0QuawaaDyYH5iBVyQCSQA2ALvJPRRQT8QgUdUEjPWs+r6QqHIGlsPdv/1UMIuuNJ3Fh4UwI8+WcAvAZQxEcJNCm2ZgOYZVpodRCPaAYblqxP0MK4wv42sA9oGJzPRLEQez8oDBfILwhHl1eAuOcL/RgZ48mF+uqhnY3dI1b781zHgBl8AKuSZEiOCe1KF2P/V1UiQBa6+Ps7OBu4w2FQi4308RmJDWCePH02K9qSCcQLuRcTncZbaIFKH7HPRe8ptmYp4A/0bUCO93lDhgg2U/RqPlag3o4toYK0JXmvoM1fW0QuIhmmEezvoVJ+sPourrpWEel2gAAAAASUVORK5CYII=");
  mask-mode: alpha;
  mask-size: 14px 14px;
  -webkit-mask-box-size: 14px 14px;
  mask-repeat: no-repeat;
  -webkit-mask-box-repeat: no-repeat;
  mask-position: center;
  -webkit-mask-box-position: center;
  background-color: var(--accent-color);
  width: 14px;
  height: 14px;
  margin: 0 1px 0 5px;
  position: relative;
  bottom: -2px;
  left: -1px;
}
div.roam-article .rm-level1 span > a.rm-alias--external:after {
  background-size: 20px 20px;
  width: 20px;
  height: 20px;
}
div.roam-article .rm-level2 span > a.rm-alias--external:after {
  background-size: 18px 18px;
  width: 18px;
  height: 18px;
}
div.roam-article .rm-level3 span > a.rm-alias--external:after {
  background-size: 16px 16px;
  width: 16px;
  height: 16px;
}

.rm-inline-references {
  background-color: var(--secondary-background-color) !important;
  border-left-color: var(--c3) !important;
  border-left-width: 3px !important;
  border-radius: 3px !important;
}

.block-ref-count-button.rm-active {
  background-color: var(--secondary-background-color) !important;
}

.rm-paren {
  color: var(--c1) !important;
  background-color: var(--secondary-background-color) !important;
  border: 1px solid var(--subtle-border-color) !important;
}

.rm-paren--closed {
  color: var(--c1) !important;
}
.rm-paren--closed path {
  fill: var(--c1) !important;
}

.rm-bq {
  background-color: var(--secondary-background-color) !important;
  border-left-color: var(--c3) !important;
  border-left-width: 3px !important;
  border-radius: 3px !important;
  padding: 8px 14px !important;
}

.block-highlight-blue {
  background-color: var(--selection-color) !important;
}

.rm-page-ref-link-color,
.rm-page-ref--link,
.rm-ref-page-view-title > a,
.rm-alias--external {
  color: var(--accent-color) !important;
}

.rm-page-ref-brackets {
  color: var(--brackets-color) !important;
}

.bp3-input {
  color: var(--c4) !important;
  background: var(--main-area-background-color) !important;
}
.bp3-input::placeholder {
  color: var(--c4) !important;
}

.bp3-elevation-3,
.confirmation-content-dialog,
.bp3-dialog {
  background: var(--popup-background-color) !important;
}

.bp3-elevation-3 div.dont-unfocus-block[style*=background] {
  background: var(--secondary-background-color) !important;
}

.bp3-dialog h2.level2 {
  color: var(--c1) !important;
}

.rm-title-untitled,
[block-input-ghost](<../block-input-ghost.md>) > span,
textarea::placeholder {
  color: var(--empty-text-color) !important;
}

.rm-all-pages .table .rm-pages-row.rm-pages-row-header {
  background: var(--page-background-color) !important;
}

body,
div,
textarea,
.level2 {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif !important;
}

iframe {
  border: none !important;
}

.loading-astrolabe {
  position: absolute !important;
  width: 80px !important;
  height: 80px !important;
  opacity: 0.3 !important;
  top: calc(50% - 40px) !important;
  left: calc(50% - 40px) !important;
}

[roam-sidebar-logo](<../roam-sidebar-logo.md>) {
  display: none !important;
}

.rm-page-ref-tag {
  color: [9099a1](<../9099a1.md>) !important;
}

span.checkmark {
  top: -2px;
}

.roam-log-container .roam-log-page {
  border-top: 1px solid var(--subtle-border-color) !important;
}
.roam-log-container .roam-log-page:first-child {
  min-height: 0 !important;
  border-top: none !important;
}

.rm-embed-container {
  border-radius: 6px !important;
}

.rm-reference-item {
  background: var(--reference-item-background) !important;
  border: 1px solid var(--subtle-border-color) !important;
  border-radius: 6px !important;
  padding: 8px 10px 8px 2px !important;
}
.rm-reference-item .rm-block-text {
  font-size: var(--font-size) !important;
}

.rm-full-width {
  margin-right: 0 !important;
}

.kanban-board {
  max-width: 100% !important;
  padding: 0 !important;
  background: none !important;
}
.kanban-board .kanban-column {
  border-radius: 6px !important;
  padding: 0 !important;
  margin: 0 !important;
}
.kanban-board .kanban-column:not([style*=background]) {
  background: transparent !important;
}
.kanban-board .kanban-column[style*=background] {
  background: var(--secondary-background-color) !important;
}
.kanban-board .kanban-column .kanban-title {
  text-align: left !important;
  border-bottom: 1px solid var(--subtle-border-color) !important;
  padding: 2px 8px !important;
  min-height: 31px;
  max-height: 31px;
  font-size: 14px !important;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.kanban-board .kanban-column .kanban-card {
  background: var(--cards-background-color) !important;
  box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.7), 0px 4px 7px -1px rgba(0, 0, 0, 0.07) !important;
  border-radius: 4px !important;
  padding: 6px 10px !important;
  margin: 0px 6px 12px !important;
  font-size: 14px !important;
}
.kanban-board .kanban-column .kanban-card .check-container {
  margin-bottom: 8px !important;
}

.bp3-popover-content div > div > .flex-h-box div > div > span,
.bp3-popover-content div > div > .flex-h-box div > div > strong,
.bp3-popover-content div > div > div > button,
.bp3-popover-content > ul > div {
  color: [182026](<../182026.md>) !important;
}

.DayPicker {
  color: [182026](<../182026.md>) !important;
}

.rm-block-ref {
  border-bottom: 0.5px solid var(--border-color) !important;
}
.rm-block-ref:hover {
  background: var(--ref-hover-bg-color) !important;
}

.CodeMirror {
  font-size: 13px !important;
}

.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .log-button:hover,
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper .starred-pages .page:hover {
  background-color: transparent !important;
  color: var(--c1) !important;
}

.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .log-button,
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper,
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper .starred-pages .page,
.bp3-minimal > div {
  color: var(--c2) !important;
  font-size: 13px !important;
}

.roam-sidebar-content {
  padding: 0 !important;
}
.roam-sidebar-content > div:not(.log-button):not(:first-child) {
  padding: 0 !important;
}
.roam-sidebar-content > div:first-child {
  padding-bottom: 18px !important;
}
.roam-sidebar-content div {
  line-height: 1.2 !important;
}
.roam-sidebar-content .rm-db-title {
  margin-top: 0 !important;
  color: var(--c2) !important;
}

[roam-right-sidebar-content](<../roam-right-sidebar-content.md>) .sidebar-content > div > div[style*=border-bottom] {
  border-bottom: 1px solid var(--subtle-border-color) !important;
}

.starred-pages-wrapper > div:first-child {
  display: none;
}
.starred-pages-wrapper .flex-h-box,
.starred-pages-wrapper .flex-h-box span {
  font-size: 13px !important;
  opacity: 0.6 !important;
}

.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .log-button,
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper .starred-pages .page {
  padding: 6px 24px 6px !important;
}
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .shortcut {
  padding: 14px 24px 0;
}
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .top-row {
  padding: 12px 0 0 20px;
}
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .top-row:hover {
  background-color: inherit;
}

.bp3-icon-small {
  padding-left: 24px !important;
}

.rm-block-text {
  max-width: 660px !important;
  font-size: var(--font-size) !important;
}

.block-bullet-view {
  margin-bottom: 3px !important;
}

.controls .simple-bullet-outer {
  margin-top: 4px !important;
}

.rm-multibar {
  border-right-color: var(--c5) !important;
}
.rm-multibar:hover {
  border-right-color: var(--c4) !important;
}

.rm-reference-main div > strong {
  color: gray !important;
}

.bp3-menu,
.bp3-popover .bp3-popover-content {
  background-color: var(--popup-background-color) !important;
}

.bp3-popover .bp3-popover-arrow-fill {
  fill: var(--popup-background-color) !important;
}

.bp3-menu,
.bp3-popover,
.bp3-popover-content,
.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown a {
  color: var(--c1) !important;
}
.bp3-menu div > div > .flex-h-box div > div > span,
.bp3-menu div > div > .flex-h-box div > div > strong,
.bp3-menu div > div > div > button,
.bp3-menu > ul > div,
.bp3-popover div > div > .flex-h-box div > div > span,
.bp3-popover div > div > .flex-h-box div > div > strong,
.bp3-popover div > div > div > button,
.bp3-popover > ul > div,
.bp3-popover-content div > div > .flex-h-box div > div > span,
.bp3-popover-content div > div > .flex-h-box div > div > strong,
.bp3-popover-content div > div > div > button,
.bp3-popover-content > ul > div,
.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown a div > div > .flex-h-box div > div > span,
.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown a div > div > .flex-h-box div > div > strong,
.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown a div > div > div > button,
.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown a > ul > div {
  color: var(--c1) !important;
}

.rm-find-or-create-wrapper .rm-menu-item .rm-search-list-item {
  color: var(--c2) !important;
}

.rm-search-path-results {
  background-color: var(--popup-background-color) !important;
}
.rm-search-path-results li {
  color: var(--c1) !important;
}

.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown {
  box-shadow: none !important;
}

.bp3-menu-item.setting {
  background: none !important;
}

.rm-menu-item[style*=background-color],
.roam-body .roam-app .roam-sidebar-container .rm-graph-dropdown .setting:hover {
  background-color: var(--secondary-background-color) !important;
}

[rm-mobile-bar](<../rm-mobile-bar.md>) {
  background-color: var(--main-area-background-color) !important;
}
[rm-mobile-bar](<../rm-mobile-bar.md>)[style*="bottom: 0px"] {
  padding-bottom: env(safe-area-inset-bottom);
  box-shadow: rgba(0, 0, 0, 0.05) 0px 0px 15px, rgba(0, 0, 0, 0.1) 0px 0px 50px !important;
}

/* Credits */
.roam-topbar > div > div:last-child ul.bp3-menu:after {
  content: "Better Roam Research theme by @linuz90";
  width: 160px;
  display: inline-block;
  font-size: 13px;
  line-height: 1.4;
  padding: 7px;
  opacity: 0.6;
  color: var(--c2);
}```
- ```css
.rm-bq {
  background-color: var(--bg-quote);
  color: var(--fg-quote);
  border-left: 1px solid var(--br-quote);
  font-size: 15.5px;
  font-style: var(--fnt-style-quote);
}```
