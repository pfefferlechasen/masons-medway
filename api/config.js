export default function handler(req, res) {
  const key = process.env.GOOGLE_MAPS_API_KEY;

  if (!key) {
    res.status(500).json({ error: 'API key not configured' });
    return;
  }

  res.status(200).json({ key });
}
