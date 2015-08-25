import os
import tempfile


def source(vim, code):
    fd, fname = tempfile.mkstemp()
    with os.fdopen(fd,'w') as f:
        f.write(code)
    vim.command('source '+fname)
    os.unlink(fname)


def apply_preview_toggle_func(vim):
    source(vim, """
        function! PyGtkTogglePreview()
            call rpcnotify({chan}, "toggle-preview", 1)
        endfunction
    """.format(chan=vim.channel_id))
    vim.command('nnoremap <leader>Q :call PyGtkTogglePreview()<CR>')


def apply_font_settings_func(vim):
    source(vim, """
        function! PyGtkSetFontSize(s)
            call rpcnotify({chan}, "font-settings-change-size", a:s)
        endfunction

        function! PyGtkSetFont(font)
            call rpcnotify({chan}, "font-settings-change-font", a:font)
        endfunction
    """.format(chan=vim.channel_id))
