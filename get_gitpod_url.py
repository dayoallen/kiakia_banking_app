tasks:
  - init: echo "Setting up environment variables"
    command: |
      export API_KEY=your_api_key
      export AUTH_TOKEN=your_auth_token
ports:
  - port: 36441
    onOpen: open-preview