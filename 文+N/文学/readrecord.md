
转至元数据结尾
由 徐仕猛创建于 2022-02-07转至元数据起始
Android客户端阅读记录的数据结构：

private int bookId;
private String bookName;//书名
private int lastVolumeId;//卷id
private int lastReadChapterId;//章节id
private String lastReadChapterName;//上次阅读章节名
private int lastReadWordCount;//阅读偏移量
private int unionId = -1;//用户id
private long lastReadTime;//上次阅读时间
private boolean isInShelf;//是否在书架中
private boolean isInHistory;//是否在阅读历史中
private String cover;
private int volumeId;
private int lastReadChapterSeqId;
private int totalChapterCount;
private long lastSyncTime;//阅读记录上次同步时间
private long lastChangedTime;//阅读记录上次修改时间

数据同步方案：

场景：到离线阅读和设备间数据同步场景，所以将服务端作为数据备份，客户端数据为主，使用了下面的同步方案：



拉取数据：

判断本地的lastSyncTime是否等于lastChangedTime

如果相等，则使用服务端的数据覆盖这条阅读记录

如果不等，则继续保留当前的这条阅读记录

时机：

打开app、打开阅读器、打开屏幕、关闭屏幕、网络变化、用户登录



上报数据：

判断lastSyncTime是否等于lastChangedTime

如果相等：则不上报

如果不等，则加入上报阅读记录

接口返回成功之后

将syncTime和changeTime改为当前时间并保存在客户端

触发时机：

打开关闭阅读器、章节结束、亮屏、息屏



这样保证了单台设备的数据不会因为离线阅读之后，再次与服务端同步之后导致的阅读记录丢失的问题

多设备之间，由于以客户端数据为主，保证了当前设备上的未同步的数据不会被服务端覆盖