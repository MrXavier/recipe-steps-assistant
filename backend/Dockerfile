FROM public.ecr.aws/lambda/python:3.10.2023.08.17.16 as builder

# Don't know if its needed
RUN yum install -y clang gcc

# Install dep for lxml lib
RUN yum install -y libxml2-devel libxslt-devel

# Install Rust to build Tiktoken lib
RUN yum install -y curl
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Python requirements
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


FROM public.ecr.aws/lambda/python:3.10.2023.08.17.16

RUN yum install -y libxml2-devel libxslt-devel

COPY --from=builder /var/lang/lib/python3.10/site-packages/ /var/lang/lib/python3.10/site-packages/
COPY . ${LAMBDA_TASK_ROOT}

CMD [ "lambda_handler.handle" ]
