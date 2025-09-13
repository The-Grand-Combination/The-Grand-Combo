Original Issues in TGC 2.5.2

If the KUK (Austro-Hungarian Empire) forms the South German Confederation, it causes the already established KUK to no longer accept the Hungarian ethnicity.
However, when such a KUK attempts to form the Danubian Federation (DNB), even if the Hungarian ethnicity fully accepts the proposal, the resulting DNB still does not accept Hungarians.

Analysis of the Original Issues

Investigation reveals that in the events folder, the Post-Formation Events group in DNBFlavor.txt does not include a follow-up event for full Hungarian agreement.
It is speculated that the TGC team discovered that applying the old template could result in a federation where Hungarians agree but the remaining Cisleithanian ethnicities do not, potentially granting the entire Cisleithania core unexpectedly.
Consequently, the TGC team removed the original event but has not yet added a revised one.

My Solution

Add a post-formation event for full Hungarian agreement with ID 98689, and manually add cores for Little Hungary based on province IDs.

Known Issues with My Solution

a: The original mod has very limited event ID availability, and event IDs in DNBFlavor.txt are strictly ordered, so the new event ID does not strictly follow the original sequence.
b: Other ethnicity events are tied to the global_flag=full_hungarian_approval, but I cannot control the timing of ID 98689 to occur last, so the flag is not recycled.

This has been tested on my computer and runs normally. If any bugs are found, please submit them.

#####################################################################################################################################################################################################################

原版TGC2.5.2的问题：
如果KUK（奥匈帝国）组建了南德意志邦联，会使已经成立的KUK不再接受匈牙利民族
但这样的KUK试图组建多瑙联邦时，即使匈牙利民族完全接受提案，组建后的DNB（多瑙联邦）也不接受匈牙利人

对原版问题的分析：
调查发现，events文件夹中DNBFlavor.txt的Post-Formation Events组中，没有做匈牙利人完全同意后续事件
推测TGC组发现若套用旧模板，匈牙利人同意而外莱塔尼亚剩余民族不同意的联邦，可能意外拥有整个外莱塔尼亚核心
猜测TGC组因此删去原有事件，但尚未增添修改后的事件

我的解决方案：
增添联邦成立后的匈牙利人完全同意后续ID98689事件，手动按省份id增加小匈牙利核心

我的方案的已知问题：
a：原mod的事件ID余量很少，且DNBFlavor.txt中事件ID排序严格，所以新增事件ID并不严格遵循原有顺序
b: 其余民族事件跟global_flag=full_hungarian_approval有关，我无法控制ID98689最后发生，所以不回收flag

已经在我的电脑测试运行正常，如有bug请提交
