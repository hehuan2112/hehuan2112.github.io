import meRaw from '../../content/works.json'
import publicationsRaw from '../../content/works.publications.json'
import projectsRaw from '../../content/works.projects.json'
import newsRaw from '../../content/works.news.json'
import awardsRaw from '../../content/works.awards.json'
import patentsRaw from '../../content/works.patents.json'
import workExpRaw from '../../content/works.work_exp.json'
import academicExpRaw from '../../content/works.academic_exp.json'
import toolsRaw from '../../content/works.tools.json'

export default {
  me: meRaw.me,
  publications: publicationsRaw.filter(p => p.title),
  projects: projectsRaw.filter(p => p.title),
  news: newsRaw.filter(n => n.date && n.text),
  awards: awardsRaw.filter(a => a.title),
  patents: patentsRaw,
  workExp: workExpRaw,
  academicExp: academicExpRaw,
  tools: toolsRaw.filter(t => t.slug),
}
