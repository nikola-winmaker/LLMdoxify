RUN git clone https://github.com/nikola-winmaker/LLMdoxify.git && \
    pip3 install -r requirements.txt && \
    mkdir -p repositories && \
    cd repositories && \
    git clone https://huggingface.co/spaces/mosaicml/mpt-30b-chat && \
    pip3 install -r exllama/requirements.txt

