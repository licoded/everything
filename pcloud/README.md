## aims

to upload files from **Github actions**, and then download them on aliyun_server machine.

the file I need to transfer is SprintBoot jar file

> why I need transfer it? It is the most clean means/approach for cloud server so that I don't need to worry about reconfig after re-install/build or change my cloud server.

## `get_url.sh`, `down_pcloud.sh`

> almost the same file/script, different about input

## `upload*.py`

`upload.py`: just upload with auth/token_str and get link/code immediately
`upload2.py`: copy curl request from Edge browser on Mac, paste it into postman, and generate python-request codes
`upload3.py`: delete other/not-current tokens
`upload4.py`: first upload, then delete other/not-current tokens
> It don't delete at first, because I find it may get Error when uploading after delete other tokens although the likehood/possibility is very low.
