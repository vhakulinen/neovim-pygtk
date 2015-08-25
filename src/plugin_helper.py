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
