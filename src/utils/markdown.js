import { marked } from 'marked'

marked.setOptions({ breaks: true })

export function md(text) {
  if (!text) return ''
  return marked.parse(text)
}

export function mdInline(text) {
  if (!text) return ''
  return marked.parseInline(text)
}

export function highlightMe(text, name = 'Huan He') {
  return text.replace(new RegExp(name, 'g'), `<strong>${name}</strong>`)
}

export function getYear(dateStr) {
  if (!dateStr) return null
  const match = dateStr.match(/\d{4}/)
  return match ? parseInt(match[0]) : null
}

function formatAuthorName(fullName) {
  const parts = fullName.trim().split(/\s+/)
  if (parts.length === 1) return parts[0]
  const lastName = parts[parts.length - 1]
  const initials = parts.slice(0, -1).map(p => p[0].toUpperCase()).join('')
  return `${lastName} ${initials}`
}

function formatAuthors(authorsStr) {
  return authorsStr.split(',').map(a => formatAuthorName(a)).join(', ')
}

export function formatCitation(pub) {
  const authors = formatAuthors(pub.authors)
  return `${authors}. ${pub.title}. <em>${pub.source}</em>. ${pub.date}.`
}
