tmux配置整理
============

:author: hackrole
:email: daipeng123456@gmail.com
:date: 2018-05-04 10:56:35
:status: draft
:tags: tmux
:category: tools

nested session
--------------

https://medium.freecodecamp.org/tmux-in-practice-local-and-nested-remote-tmux-sessions-4f7ba5db8795

操作内部tmux方案

1) send-prefix C-q

2) use different prefix
.. code-block:: tmux

    set -g prefix C-b
    bind-key -n C-a send-prefix

3) use a toggle key
.. code-block:: tmux

    bind -T root F12  \
    set prefix None \;\
    set key-table off \;\
    set status-style "fg=$color_status_text,bg=$color_window_off_status_bg" \;\
    set window-status-current-format "#[fg=$color_window_off_status_bg,bg=$color_window_off_status_current_bg]$separator_powerline_right#[default] #I:#W# #[fg=$color_window_off_status_current_bg,bg=$color_window_off_status_bg]$separator_powerline_right#[default]" \;\
    set window-status-current-style "fg=$color_dark,bold,bg=$color_window_off_status_current_bg" \;\
    if -F '#{pane_in_mode}' 'send-keys -X cancel' \;\
    refresh-client -S \;\

    bind -T off F12 \
    set -u prefix \;\
    set -u key-table \;\
    set -u status-style \;\
    set -u window-status-current-style \;\
    set -u window-status-current-format \;\
    refresh-client -S

    wg_is_keys_off="#[fg=$color_light,bg=$color_window_off_indicator]#([ $(tmux show-option -qv key-table) = 'off' ] && echo 'OFF')#[default]"

    set -g status-right "$wg_is_keys_off #{sysstat_cpu} | #{sysstat_mem} | #{sysstat_loadavg} | $wg_user_host"
