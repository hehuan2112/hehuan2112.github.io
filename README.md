# Huan He's Online CV

Welcome! and thank you so much for viewing my online CV! You can visit the [hehuan2112.github.io](https://hehuan2112.github.io/) to view the CV.

# Update

It has been a super big update since 2023!
I learned to use [Pelican](https://getpelican.com/) to manage the HTML rendering and to make a easy-to-write enviroment for me. 

# Deployment

To deploy the generated static site on GitHub Pages, the following steps should be followed:

1. Enable workflow permissions. In "Settings / Action / General", ensure the "Workflow permissions" is set to "Read and write permissions".
2. Enable GitHub Action and add a new workflow `main.yml`. 
   Copy the following content to create the workflow action. 
   It will take a few minutes to run. Once it shows completed without any error in the Action, you can move next step.
3. Enable the GitHub Pages. In "Settings / Pages", select:
    - Source: Deploy from a branch
    - Branch: gh-pages, /(root)

If everything works fine, you can find the `gh-pages` branch has been deployed on GitHub Pages and you can access it.

```yaml
# This is a basic workflow to help you get started with Actions

name: Deploy Latest Pages by Pelican

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "master" branch
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, Pelican!
          
      # Runs a build for pelican
      - name: GitHub Pages Pelican Build Action
        uses: nelsonjchen/gh-pages-pelican-action@0.1.10
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

# Update publications and others

To add a new publication, add the following code in the `publications` of `content/works.publications.json` and edit the content accordingly:

```json
{
    "thumb": "",
    "title": "",
    "authors": "",
    "date": "",
    "source": "",
    "links": [
        ["", "", "paper"]
    ]
},
```

Similar to publication, add the following in the `content/works.projects.json` to add a new project:

```json
{
    "slug": "",
    "date": "",
    "thumb": "",
    "title": "",
    "organization": "",
    "location": "",
    "description": "",
    "links": [
        ["", "", "demo"]
    ]
}
```

Also thanks the [Milligram](https://milligram.io/)!
